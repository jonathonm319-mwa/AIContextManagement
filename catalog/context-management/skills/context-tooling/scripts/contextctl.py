#!/usr/bin/env python3
from __future__ import annotations
import argparse
import datetime as dt
import json
import os
from pathlib import Path
from typing import Any, Dict, List

HOME = Path.home()
ROOT = HOME / '.ai-context'
REGISTRY = ROOT / 'registry' / 'projects.json'
PROJECTS = ROOT / 'projects'
SESSIONS = ROOT / 'sessions'
TEMPLATES = ROOT / 'templates'


def utcnow() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def ensure_dirs() -> None:
    (ROOT / 'registry').mkdir(parents=True, exist_ok=True)
    PROJECTS.mkdir(parents=True, exist_ok=True)
    SESSIONS.mkdir(parents=True, exist_ok=True)
    TEMPLATES.mkdir(parents=True, exist_ok=True)
    if not REGISTRY.exists():
        REGISTRY.write_text(json.dumps({'projects': []}, indent=2), encoding='utf-8')
    template = TEMPLATES / 'project-state.template.json'
    if not template.exists():
        template.write_text(json.dumps(default_state('sample-project', 'Sample Project'), indent=2), encoding='utf-8')


def default_state(project: str, title: str) -> Dict[str, Any]:
    return {
        'project': project,
        'title': title,
        'task': {
            'title': title,
            'description': ''
        },
        'state': {
            'completed': [],
            'in_progress': [],
            'not_started': []
        },
        'decisions': [],
        'open_questions': [],
        'next_actions': [],
        'constraints': [],
        'references': {
            'repos': [],
            'files': [],
            'docs': []
        },
        'mental_model': '',
        'summary': '',
        'related_projects': [],
        'last_updated': utcnow(),
        'created': utcnow(),
        'history': []
    }


def load_registry() -> Dict[str, Any]:
    ensure_dirs()
    return json.loads(REGISTRY.read_text(encoding='utf-8'))


def save_registry(data: Dict[str, Any]) -> None:
    REGISTRY.write_text(json.dumps(data, indent=2), encoding='utf-8')


def project_dir(slug: str) -> Path:
    return PROJECTS / slug


def state_path(slug: str) -> Path:
    return project_dir(slug) / 'state.json'


def load_state(slug: str) -> Dict[str, Any]:
    p = state_path(slug)
    if not p.exists():
        raise SystemExit(f'Project not found: {slug}')
    return json.loads(p.read_text(encoding='utf-8'))


def save_state(slug: str, state: Dict[str, Any]) -> None:
    d = project_dir(slug)
    d.mkdir(parents=True, exist_ok=True)
    state['last_updated'] = utcnow()
    state_path(slug).write_text(json.dumps(state, indent=2), encoding='utf-8')


def add_unique(items: List[str], additions: List[str]) -> List[str]:
    existing = list(items)
    for item in additions:
        item = item.strip()
        if item and item not in existing:
            existing.append(item)
    return existing


def cmd_init(args: argparse.Namespace) -> None:
    ensure_dirs()
    slug = args.project.strip()
    title = args.title.strip() if args.title else slug
    p = state_path(slug)
    if not p.exists():
        save_state(slug, default_state(slug, title))
    reg = load_registry()
    if slug not in reg['projects']:
        reg['projects'].append(slug)
        reg['projects'].sort()
        save_registry(reg)
    print(f'Initialized project: {slug}')
    print(str(state_path(slug)))


def cmd_list(args: argparse.Namespace) -> None:
    reg = load_registry()
    rows = []
    for slug in reg.get('projects', []):
        try:
            st = load_state(slug)
            rows.append({
                'project': slug,
                'title': st.get('title', slug),
                'last_updated': st.get('last_updated', ''),
                'next_actions': len(st.get('next_actions', [])),
                'related_projects': len(st.get('related_projects', []))
            })
        except SystemExit:
            rows.append({'project': slug, 'title': slug, 'last_updated': '', 'next_actions': 0, 'related_projects': 0})
    print(json.dumps(rows, indent=2))


def cmd_resume(args: argparse.Namespace) -> None:
    st = load_state(args.project)
    out = {
        'project': st['project'],
        'title': st.get('title', st['project']),
        'summary': st.get('summary', ''),
        'mental_model': st.get('mental_model', ''),
        'task': st.get('task', {}),
        'state': st.get('state', {}),
        'decisions': st.get('decisions', []),
        'open_questions': st.get('open_questions', []),
        'next_actions': st.get('next_actions', [])[:10],
        'constraints': st.get('constraints', []),
        'references': st.get('references', {}),
        'related_projects': st.get('related_projects', []),
        'last_updated': st.get('last_updated', '')
    }
    print(json.dumps(out, indent=2))


def cmd_checkpoint(args: argparse.Namespace) -> None:
    st = load_state(args.project)
    if args.title:
        st['title'] = args.title.strip()
        st.setdefault('task', {})['title'] = args.title.strip()
    if args.description:
        st.setdefault('task', {})['description'] = args.description.strip()
    if args.summary:
        st['summary'] = args.summary.strip()
    if args.mental_model:
        st['mental_model'] = args.mental_model.strip()

    st.setdefault('state', {})
    st['state']['completed'] = add_unique(st['state'].get('completed', []), args.completed or [])
    st['state']['in_progress'] = add_unique(st['state'].get('in_progress', []), args.in_progress or [])
    st['state']['not_started'] = add_unique(st['state'].get('not_started', []), args.not_started or [])
    st['decisions'] = add_unique(st.get('decisions', []), args.decision or [])
    st['open_questions'] = add_unique(st.get('open_questions', []), args.question or [])
    st['next_actions'] = add_unique([], args.next_action or []) + [x for x in st.get('next_actions', []) if x not in (args.next_action or [])]
    st['constraints'] = add_unique(st.get('constraints', []), args.constraint or [])

    refs = st.setdefault('references', {'repos': [], 'files': [], 'docs': []})
    refs['repos'] = add_unique(refs.get('repos', []), args.repo or [])
    refs['files'] = add_unique(refs.get('files', []), args.file or [])
    refs['docs'] = add_unique(refs.get('docs', []), args.doc or [])

    entry = {
        'timestamp': utcnow(),
        'summary': args.summary or '',
        'completed': args.completed or [],
        'in_progress': args.in_progress or [],
        'not_started': args.not_started or [],
        'decisions': args.decision or [],
        'open_questions': args.question or [],
        'next_actions': args.next_action or [],
        'constraints': args.constraint or [],
        'references': {
            'repos': args.repo or [],
            'files': args.file or [],
            'docs': args.doc or []
        }
    }
    st.setdefault('history', []).append(entry)
    save_state(args.project, st)

    now = dt.datetime.now(dt.timezone.utc)
    session_dir = SESSIONS / now.strftime('%Y') / now.strftime('%Y-%m-%d')
    session_dir.mkdir(parents=True, exist_ok=True)
    session_file = session_dir / f"{now.strftime('%Y%m%dT%H%M%SZ')}-{args.project}.json"
    session_file.write_text(json.dumps(entry, indent=2), encoding='utf-8')

    print(json.dumps({'saved': True, 'state': str(state_path(args.project)), 'session': str(session_file)}, indent=2))


def cmd_focus(args: argparse.Namespace) -> None:
    st = load_state(args.project)
    next_actions = st.get('next_actions', [])
    completed = set(st.get('state', {}).get('completed', []))
    prioritized = [x for x in next_actions if x not in completed]
    output = {
        'project': args.project,
        'top_next_actions': prioritized[: args.limit],
        'open_questions': st.get('open_questions', [])[:5],
        'recent_summary': st.get('summary', ''),
        'last_updated': st.get('last_updated', '')
    }
    print(json.dumps(output, indent=2))


def cmd_link(args: argparse.Namespace) -> None:
    st = load_state(args.project)
    other = args.related_project.strip()
    st['related_projects'] = add_unique(st.get('related_projects', []), [other])
    save_state(args.project, st)

    try:
        st2 = load_state(other)
        st2['related_projects'] = add_unique(st2.get('related_projects', []), [args.project])
        save_state(other, st2)
    except SystemExit:
        pass

    print(json.dumps({'linked': [args.project, other]}, indent=2))


def cmd_prune(args: argparse.Namespace) -> None:
    reg = load_registry()
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=args.days)
    stale = []
    for slug in reg.get('projects', []):
        try:
            st = load_state(slug)
            lu = st.get('last_updated')
            if not lu:
                stale.append({'project': slug, 'reason': 'missing-last-updated'})
                continue
            ts = dt.datetime.strptime(lu, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=dt.timezone.utc)
            if ts < cutoff:
                stale.append({'project': slug, 'last_updated': lu})
        except Exception as ex:
            stale.append({'project': slug, 'reason': str(ex)})
    print(json.dumps({'days': args.days, 'stale_projects': stale}, indent=2))


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description='Global AI context store controller')
    sub = p.add_subparsers(dest='command', required=True)

    x = sub.add_parser('init')
    x.add_argument('--project', required=True)
    x.add_argument('--title')
    x.set_defaults(func=cmd_init)

    x = sub.add_parser('list')
    x.set_defaults(func=cmd_list)

    x = sub.add_parser('resume')
    x.add_argument('--project', required=True)
    x.set_defaults(func=cmd_resume)

    x = sub.add_parser('checkpoint')
    x.add_argument('--project', required=True)
    x.add_argument('--title')
    x.add_argument('--description')
    x.add_argument('--summary')
    x.add_argument('--mental-model', dest='mental_model')
    x.add_argument('--completed', action='append')
    x.add_argument('--in-progress', dest='in_progress', action='append')
    x.add_argument('--not-started', dest='not_started', action='append')
    x.add_argument('--decision', action='append')
    x.add_argument('--question', action='append')
    x.add_argument('--next-action', dest='next_action', action='append')
    x.add_argument('--constraint', action='append')
    x.add_argument('--repo', action='append')
    x.add_argument('--file', action='append')
    x.add_argument('--doc', action='append')
    x.set_defaults(func=cmd_checkpoint)

    x = sub.add_parser('focus')
    x.add_argument('--project', required=True)
    x.add_argument('--limit', type=int, default=3)
    x.set_defaults(func=cmd_focus)

    x = sub.add_parser('link')
    x.add_argument('--project', required=True)
    x.add_argument('--related-project', required=True)
    x.set_defaults(func=cmd_link)

    x = sub.add_parser('prune')
    x.add_argument('--days', type=int, default=30)
    x.set_defaults(func=cmd_prune)

    return p


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
