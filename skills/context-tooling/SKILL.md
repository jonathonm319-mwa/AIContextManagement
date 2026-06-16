---
name: context-tooling
description: >
  Foundational tooling for a global AI context store in ~/.ai-context. Use when you need to initialize projects, list them, resume from saved state, save a checkpoint, focus next actions, link projects, or identify stale project context.
---
# Context Tooling

This skill provides the script used by the other context skills.

## Script location

- Linux/macOS: `~/.copilot/skills/context-tooling/scripts/contextctl.py`
- Windows PowerShell: `$HOME/.copilot/skills/context-tooling/scripts/contextctl.py`

## Supported commands

- `init`
- `list`
- `resume`
- `checkpoint`
- `focus`
- `link`
- `prune`

## Command examples

### Initialize a project

```bash
python ~/.copilot/skills/context-tooling/scripts/contextctl.py init --project dev-proxy --title "Dev Proxy"
```

### Resume a project

```bash
python ~/.copilot/skills/context-tooling/scripts/contextctl.py resume --project dev-proxy
```

### Save a checkpoint

```bash
python ~/.copilot/skills/context-tooling/scripts/contextctl.py checkpoint   --project dev-proxy   --summary "Wired proxy to local app and identified remaining retry test work."   --completed "Created initial proxy config"   --in-progress "Validate interception for /disbursements"   --decision "Use proxy override instead of changing service discovery"   --question "Should proxy run inside Aspire or outside it?"   --next-action "Run interception smoke test"   --next-action "Add 429 failure simulation"   --file "src/Web/Program.cs"   --doc "internal/dev-proxy-notes"
```
