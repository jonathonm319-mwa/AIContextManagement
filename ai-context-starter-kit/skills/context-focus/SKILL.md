---
name: context-focus
description: >
  Produces a prioritized restart plan from ~/.ai-context. Use when the user asks what to do next, how to resume efficiently, or how to prioritize work after an interruption.
---
# Context Focus

## Goal

Convert saved context into the smallest useful next moves.

## Procedure

1. Determine the project slug.
2. Run:

```bash
python ~/.copilot/skills/context-tooling/scripts/contextctl.py focus --project <slug> --limit 3
```

3. Return:
   - top 3 next actions
   - any open questions blocking progress
   - a one-paragraph rationale for ordering

## Rules

- Favor reversible actions first.
- Favor actions that reduce uncertainty.
- If the store is stale, say so and recommend a refresh checkpoint.
