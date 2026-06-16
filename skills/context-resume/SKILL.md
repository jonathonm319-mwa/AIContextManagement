---
name: context-resume
description: >
  Reloads a saved project checkpoint from ~/.ai-context and reconstructs the user’s working state. Use when the user asks to resume work, continue, recall previous work, reload context, or figure out where they left off.
---
# Context Resume

## Goal

Rehydrate a project into an actionable resume packet.

## Procedure

1. Determine the project slug.
   - Prefer an explicit project name from the prompt.
   - If missing, infer from the active workspace folder name.
   - If still ambiguous, run `list` and show the likely candidates.
2. Check that the project is initialized (see the agent's **Check initialization** behavior). If it is not in the registry, follow the initialization flow before continuing.
3. Run:

```bash
python ~/.copilot/skills/context-tooling/scripts/contextctl.py resume --project <slug>
```

3. Present the result in this structure:
   - Goal
   - Current state
   - Decisions already made
   - Open questions
   - Top next actions
   - Related projects
   - Last updated

## Rules

- Prefer concise bullets over long prose.
- Optimize for fast re-entry.
- Do not dump raw JSON back to the user unless they ask for it.
