# Installation and Setup

## Prerequisites

- GitHub Copilot with agent capabilities in a supported editor
- A Python runtime available on the machine
- Personal skill support enabled in your environment

## Step 1: Place skills in the user profile

Copy the skills into the personal skills folder:

- Linux/macOS: `~/.copilot/skills/`
- Windows PowerShell: `$HOME/.copilot/skills/`

Required skill folders:

- `context-tooling`
- `context-resume`
- `context-checkpoint`
- `context-focus`
- `context-maintenance`

## Step 2: Create the custom agent in the user profile

Use the custom agent configuration UI to create a user-profile agent named **Context Orchestrator**.

The agent should:

- specialize in momentum preservation
- treat `~/.ai-context` as the source of truth for task-state
- activate resume, checkpoint, focus, and maintenance skills when relevant

## Step 3: Initialize the first project

Example:

```bash
python ~/.copilot/skills/context-tooling/scripts/contextctl.py init --project foundry-project --title "Foundry Project"
```

This initializes the global store and creates a project state file.

## Step 4: Use the system in normal work

Examples:

```text
@Context Orchestrator resume work on foundry-project
@Context Orchestrator checkpoint this session
@Context Orchestrator what are my top next actions for foundry-project?
@Context Orchestrator list stale projects
```

## Suggested local conventions

Define a consistent project slug strategy:

- use lowercase
- use hyphens instead of spaces
- keep slugs stable over time

Recommended examples:

- `foundry-project`
- `aspire-hosting`
- `dev-proxy`
- `terraform-foundry`
