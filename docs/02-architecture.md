# Architecture

## Core architecture pattern

The architecture follows a simple principle:

> **Skills provide capability, the custom agent provides orchestration, and the external store provides memory.**

## Components

### 1. Global context store

**Location:** `~/.ai-context`

This is the source of truth for dynamic work state.

Responsibilities:

- persist project-level working context
- persist session snapshots/checkpoints
- support cross-project continuity
- remain independent of any single git repository

Suggested layout:

```text
~/.ai-context/
  registry/
    projects.json
  projects/
    <project-slug>/
      state.json
  sessions/
    <year>/
      <date>/
        <timestamp>-<project-slug>.json
  templates/
    project-state.template.json
```

### 2. User-profile custom agent

The custom agent acts as the **context orchestrator**.

Responsibilities:

- identify when work should be resumed from saved state
- identify when progress should be checkpointed
- present concise restart packets
- surface next actions and blockers
- route maintenance tasks to the appropriate skill

### 3. Personal Agent Skills

Skills are global capabilities stored outside of repositories.

Implemented skills:

- `context-tooling`
- `context-resume`
- `context-checkpoint`
- `context-focus`
- `context-maintenance`

Responsibilities by skill:

#### `context-tooling`
Provides the reusable script and command surface for context operations.

#### `context-resume`
Loads existing project state and reconstructs an actionable summary.

#### `context-checkpoint`
Compresses the current session into durable work state.

#### `context-focus`
Turns saved state into the top next actions.

#### `context-maintenance`
Lists projects, links related efforts, and finds stale context.

### 4. Context control script

The `contextctl.py` script is the persistence tool used by the skills.

Current commands:

- `init`
- `list`
- `resume`
- `checkpoint`
- `focus`
- `link`
- `prune`

## Information flow

### Resume flow

1. User asks to resume work
2. Agent determines the project slug
3. Resume skill calls the tooling script
4. Project state is loaded from `~/.ai-context`
5. Agent returns a concise resume packet

### Checkpoint flow

1. User asks to save or checkpoint progress
2. Agent compresses the session into high-signal fields
3. Checkpoint skill calls the tooling script
4. Project state is updated
5. A session snapshot is also written for historical reference

### Focus flow

1. User asks what to do next
2. Focus skill loads project state
3. Next actions are prioritized
4. Agent returns a short plan for restarting work
