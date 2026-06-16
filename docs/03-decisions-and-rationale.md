# Decisions and Rationale

This document records the major design decisions made for the AI context system.

## Decision 1: Store dynamic session state outside git repositories

**Decision:** Use `~/.ai-context` as the source of truth for working context.

**Rationale:**

- the context needs to cross repository boundaries
- active task state should not pollute source repositories
- personal working memory is often broader than a single project
- some context is useful even when there is no dedicated repository yet

**Trade-off:**

- external state is less visible to teammates by default
- extra setup is required on each machine

## Decision 2: Use a custom agent plus skills instead of instructions only

**Decision:** Use a user-profile custom agent for orchestration and personal skills for reusable behaviors.

**Rationale:**

- the custom agent defines the persistent persona and operating model
- skills are better for task-specific reusable workflows
- instructions alone are not a good fit for evolving session state
- skills can include scripts and resources, not just prose guidance

**Trade-off:**

- this is slightly more complex than a single instructions file
- it introduces multiple moving parts that need to be kept aligned

## Decision 3: Keep `copilot-instructions.md` for static guidance only

**Decision:** Do not use repository instructions as the primary task-state store.

**Rationale:**

- repository instructions are most valuable for coding standards, build conventions, and project guidance
- dynamic work state changes too often and does not belong in always-on instructions
- repository instructions do not naturally model checkpoint history, open questions, or next actions

## Decision 4: Prefer compressed summaries over raw conversation transcripts

**Decision:** Save only structured, actionable context.

**Rationale:**

- raw transcripts are noisy and expensive to re-read
- resumability depends on signal, not volume
- the most valuable stored data is usually:
  - current goal
  - current state
  - decisions made
  - open questions
  - next actions

## Decision 5: Use JSON for the first implementation

**Decision:** Use JSON-backed state files in the initial version.

**Rationale:**

- the included script can remain dependency-free
- JSON is easy to serialize and inspect
- Python can manage it without external packages

**Trade-off:**

- YAML is more human-friendly for some workflows
- JSON comments are not supported

## Decision 6: Keep user memory separate from active work state

**Decision:** Treat built-in agent memory as a place for durable preferences and habits, not project task-state.

**Rationale:**

- active project state needs explicit structure and direct control
- long-lived preferences are a different class of information than live work checkpoints
- separating the two reduces ambiguity about the source of truth

## Decision 7: Capture both project state and session snapshots

**Decision:** Maintain a latest project state plus timestamped session artifacts.

**Rationale:**

- the latest state is ideal for quick restart
- session snapshots provide traceability and historical progression
- this makes it easier to detect drift or recover earlier thinking
