# Context Schema

## Project state object

The project state is the main persisted document for a project.

Example structure:

```json
{
  "project": "foundry-project",
  "title": "Foundry Project",
  "task": {
    "title": "Foundry Project",
    "description": ""
  },
  "state": {
    "completed": [],
    "in_progress": [],
    "not_started": []
  },
  "decisions": [],
  "open_questions": [],
  "next_actions": [],
  "constraints": [],
  "references": {
    "repos": [],
    "files": [],
    "docs": []
  },
  "mental_model": "",
  "summary": "",
  "related_projects": [],
  "last_updated": "2026-06-16T00:00:00Z",
  "created": "2026-06-16T00:00:00Z",
  "history": []
}
```

## Field intent

### `project`
Stable project slug used as the primary lookup key.

### `title`
Human-friendly display name.

### `task`
The current high-level problem being solved.

### `state.completed`
Things that are now done and true.

### `state.in_progress`
Things actively underway and not yet complete.

### `state.not_started`
Known work that still remains untouched.

### `decisions`
Important decisions already made and worth preserving.

### `open_questions`
Questions or uncertainties that still need to be resolved.

### `next_actions`
The most important executable follow-up actions.

### `constraints`
Important conditions, guardrails, or environmental limits.

### `references`
Links to important repos, files, or documents.

### `mental_model`
A compressed explanation of how the relevant pieces fit together.

### `summary`
A concise narrative summary of the current state.

### `related_projects`
Project slugs that should be considered nearby context.

### `history`
Checkpoint entries in chronological order.

## Session snapshot object

A session snapshot records a checkpoint event.

Example structure:

```json
{
  "timestamp": "2026-06-16T18:00:00Z",
  "summary": "Wired the local proxy configuration and identified remaining interception work.",
  "completed": ["Created initial proxy config"],
  "in_progress": ["Validate interception path"],
  "not_started": ["Add failure simulation cases"],
  "decisions": ["Use base URL override instead of rewriting service discovery"],
  "open_questions": ["Should the proxy run inside Aspire or beside it?"],
  "next_actions": ["Run interception smoke test", "Add 429 failure simulation"],
  "constraints": ["Must work locally without changing downstream API"],
  "references": {
    "repos": ["github.com/example/project"],
    "files": ["src/Web/Program.cs"],
    "docs": ["internal/dev-proxy-notes"]
  }
}
```
