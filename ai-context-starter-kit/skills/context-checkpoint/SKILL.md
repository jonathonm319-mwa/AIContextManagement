---
name: context-checkpoint
description: >
  Saves a compressed, actionable checkpoint to ~/.ai-context. Use when the user asks to save progress, checkpoint the session, summarize progress for later, or before switching tasks.
---
# Context Checkpoint

## Goal

Persist momentum, not transcripts.

## Procedure

1. Compress the conversation into the following fields:
   - summary
   - completed
   - in progress
   - not started
   - decisions
   - open questions
   - next actions
   - constraints
   - references
   - mental model (optional when useful)
2. Run a `checkpoint` command.

### Example

```bash
python ~/.copilot/skills/context-tooling/scripts/contextctl.py checkpoint   --project <slug>   --summary "<two sentence summary>"   --completed "<completed item>"   --in-progress "<in progress item>"   --decision "<important decision>"   --question "<open question>"   --next-action "<next action>"   --file "<important file>"   --doc "<important doc>"
```

## Rules

- Always include at least one next action.
- Prefer atomic next actions.
- Record facts and decisions separately from assumptions.
- Use short, high-signal summaries.
