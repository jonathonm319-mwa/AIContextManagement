# Context Management Collection

This collection provides a complete context continuity workflow for Copilot:

- A user-profile agent (`Context Orchestrator`) that coordinates usage
- Four operational skills (`context-resume`, `context-checkpoint`, `context-focus`, `context-maintenance`)
- A foundational tooling skill (`context-tooling`) with `contextctl.py`

## Use case

Use this collection when you want durable, actionable context across sessions, repos, and projects using a global store at `~/.ai-context`.

## How the pieces fit

- **Agent entrypoint**: `Context Orchestrator`
- **Operational skills**: resume, checkpoint, focus, maintenance
- **Foundation**: `context-tooling` provides the shared script used by the operational skills

The agent routes user intents to the right operational skill, while all skills rely on the tooling layer for store operations.

## Install

### Option A: bootstrap with install scripts

- Linux/macOS: `bash install.sh`
- Windows PowerShell: `.\install.ps1`

### Option B: manual install

1. Copy `catalog/context-management/skills/*` to `~/.copilot/skills`.
2. In VS Code, create a User profile custom agent and paste:
   `catalog/context-management/agents/context-orchestrator/context-orchestrator.agent.md`

## Suggested prompts

- `@Context Orchestrator resume work on foundry-project`
- `@Context Orchestrator checkpoint this session`
- `@Context Orchestrator what are my top next actions for dev-proxy?`
- `@Context Orchestrator link dev-proxy with aspire-hosting`
- `@Context Orchestrator list stale projects`
