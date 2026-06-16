# Maintenance and Evolution

## Ongoing maintenance tasks

### Keep slugs stable

Avoid renaming project slugs unless necessary. Stable lookups reduce confusion and simplify linking.

### Refresh stale projects

Use the maintenance capability to identify stale projects and refresh them when work resumes.

### Keep next actions current

The usefulness of the whole system depends heavily on the quality of `next_actions`.

Update them whenever:

- a task is completed
- a blocker changes
- a new dependency is discovered
- the work plan changes materially

### Link related projects deliberately

Use `related_projects` when:

- one project depends on another
- multiple efforts share architecture or infrastructure
- work regularly cross-references the same mental model

## Common failure modes

### Failure mode 1: Storing too much noise

If checkpoints become verbose transcripts, re-entry value drops.

**Mitigation:** keep summaries compressed and action-oriented.

### Failure mode 2: Missing next actions

Without next actions, the user still has to spend time deciding how to restart.

**Mitigation:** require at least one atomic next action in every checkpoint.

### Failure mode 3: Stale context

If the store is not maintained, trust in the system declines.

**Mitigation:** refresh at resume time and checkpoint before switching away.

### Failure mode 4: Mixing preferences with task-state

This creates ambiguity about what should be auto-applied versus what should be explicitly resumed.

**Mitigation:** keep durable preferences in memory/instructions and active work state in `~/.ai-context`.

## Recommended roadmap

### Near-term improvements

1. add richer validation for state files
2. add project archival and cleanup workflows
3. add aliases for common project lookup patterns
4. add better stale-context heuristics

### Mid-term improvements

1. move from script-driven commands to a dedicated MCP server
2. add semantic search over summaries and decisions
3. add improved cross-project recommendation logic
4. add automatic prompt suggestions when context switching is detected

### Long-term improvements

1. support machine-to-machine sync of the context store
2. support selective team-shared context
3. build richer dashboards for active projects and restart queues
