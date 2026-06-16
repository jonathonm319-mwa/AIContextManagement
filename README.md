# AI Context Starter Kit

This starter kit gives you a **global, git-independent context system** for GitHub Copilot / VS Code agents.

## What is included

- A **custom agent** that acts as a context orchestrator
- Four **personal skills** for resuming work, saving checkpoints, focusing next actions, and maintaining the store
- A lightweight **JSON-based context store** under `~/.ai-context`
- A `contextctl.py` script that manages project state and session snapshots

## Recommended architecture

- **Source of truth**: `~/.ai-context`
- **Behavior / orchestration**: user-profile custom agent
- **Reusable capabilities**: personal Agent Skills in `~/.copilot/skills`
- **Stable preferences only**: built-in user memory / Copilot Memory

## Install

### 1) Run the install script

The install script copies the skills into your personal skills folder and initializes the global context store in one step.

#### Linux/macOS

```bash
bash install.sh
```

#### Windows PowerShell

```powershell
.\install.ps1
```

The script will prompt you for a project slug and title, then set up `~/.ai-context` automatically.

### 2) Create the custom agent in your VS Code user profile

In VS Code:

1. Open Copilot Chat
2. Open the agents dropdown
3. Choose **Configure Custom Agents...**
4. Create a **User profile** agent
5. Paste the contents of `user-profile-agent/context-orchestrator.agent.md`

## Suggested prompts

- `@Context Orchestrator resume work on foundry-project`
- `@Context Orchestrator checkpoint this session`
- `@Context Orchestrator what are my top next actions for dev-proxy?`
- `@Context Orchestrator link dev-proxy with aspire-hosting`
- `@Context Orchestrator list stale projects`

## Store layout

```text
~/.ai-context/
  registry/
    projects.json
  projects/
    <slug>/
      state.json
  sessions/
    2026/
      2026-06-16/
        20260616T120000Z-<slug>.json
  templates/
    project-state.template.json
```

## Design principles

1. **Compressed, actionable context over raw logs**
2. **Always store next actions**
3. **Keep facts separate from uncertainties**
4. **Prefer the external store over repo-local instructions for cross-project continuity**
5. **Use built-in memory only for durable preferences, not task-state**
