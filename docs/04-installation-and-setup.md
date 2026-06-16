# Installation and Setup

## Prerequisites

- GitHub Copilot with agent capabilities in a supported editor
- A Python runtime available on the machine
- Personal skill support enabled in your environment

## Step 1: Run the install script

The install script copies all skill folders into your personal skills folder and initializes the global context store in one step.

#### Linux/macOS

```bash
bash install.sh
```

#### Windows PowerShell

```powershell
.\install.ps1
```

When prompted, enter a project slug (e.g. `foundry-project`) and a title. The script creates `~/.copilot/skills/` (if it does not exist), copies the five skill directories, and runs `contextctl.py init` for you.

## Step 2: Create the custom agent in the user profile

Use the custom agent configuration UI to create a user-profile agent named **Context Orchestrator**.

The agent should:

- specialize in momentum preservation
- treat `~/.ai-context` as the source of truth for task-state
- activate resume, checkpoint, focus, and maintenance skills when relevant

## Step 3: Use the system in normal work

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
