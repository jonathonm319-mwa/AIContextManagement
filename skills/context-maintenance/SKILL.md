---
name: context-maintenance
description: >
  Maintains the global context store in ~/.ai-context. Use when the user asks to list active projects, link related projects, inspect stale items, or clean up older context.
---
# Context Maintenance

## Supported tasks

### List projects

```bash
python ~/.copilot/skills/context-tooling/scripts/contextctl.py list
```

### Link projects

```bash
python ~/.copilot/skills/context-tooling/scripts/contextctl.py link --project <slug> --related-project <other-slug>
```

### Find stale projects

```bash
python ~/.copilot/skills/context-tooling/scripts/contextctl.py prune --days 30
```

## Rules

- Use linking when projects share architecture, dependencies, or business flow.
- Treat stale-project reports as a prompt to refresh, not delete, unless the user asks to archive or remove data.
