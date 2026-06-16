# Operating Model

## Daily workflow

### Session start

At the beginning of a work session:

1. identify the current project slug
2. ask the Context Orchestrator to resume work
3. review:
   - summary
   - current state
   - open questions
   - top next actions
4. begin with the highest-leverage next action

### During the session

The agent should help maintain the current state of work by tracking:

- completed work
- active work in progress
- newly made decisions
- outstanding uncertainties
- references worth preserving

### Before switching tasks

Before ending or interrupting a session, save a checkpoint.

A good checkpoint should answer:

- what changed during this session?
- what is now true?
- what is still unknown?
- what should happen next?

### When returning later

Ask the agent to resume the project. The system should minimize restart overhead by surfacing:

- the goal
- the latest summary
- decisions already made
- open questions
- prioritized next actions

## Recommended prompting patterns

### Resume prompts

- `resume work on <project>`
- `reload context for <project>`
- `pick up where I left off on <project>`

### Checkpoint prompts

- `checkpoint this session for <project>`
- `save my progress on <project>`
- `summarize this work so I can come back later`

### Focus prompts

- `what should I do next for <project>?`
- `give me the top 3 next actions for <project>`
- `help me restart after interruption`

### Maintenance prompts

- `list my active projects`
- `link <project-a> with <project-b>`
- `show me stale projects`

## Quality bar for checkpoints

Every stored checkpoint should, at minimum, contain:

- one concise summary
- at least one next action
- at least one statement of current state
- key decisions if any were made
- open questions if uncertainty remains

## What not to store

Avoid storing:

- raw chat logs
- repetitive low-value details
- transient information with no likely restart value
- instructions that belong in repository guidance instead
