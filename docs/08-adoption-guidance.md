# Adoption Guidance

## Recommended rollout strategy

### Phase 1: Personal adoption

Start with only a handful of active projects.

Suggested first use cases:

- one primary development project
- one infrastructure project
- one exploratory or planning project

The goal is to learn the checkpointing habit without too much overhead.

### Phase 2: Normalize checkpoint quality

Create a consistent standard for saved checkpoints.

A simple rule:

- one summary
- three to five meaningful state items
- one to three next actions
- any decisions or open questions that matter

### Phase 3: Cross-project linking

Once basic use is comfortable, begin linking related projects so resume packets can hint at nearby work.

Examples:

- an Aspire host linked to a downstream Dev Proxy effort
- an Azure Foundry project linked to Terraform provisioning work
- an application project linked to a security or RBAC effort

### Phase 4: Automation and enhancements

After the workflow proves useful, consider upgrading the persistence layer to an MCP server and adding smarter discovery features.

## Recommended naming conventions

### Project slugs

Use a short, stable slug:

- lowercase
- hyphen-delimited
- descriptive but not overly long

Examples:

- `azure-foundry`
- `dev-proxy`
- `claims-modernization`
- `entra-rbac`

### State item phrasing

Phrase state and next action items as concrete statements.

Good:

- `Configured base URL override in local app settings`
- `Validate interception for /disbursements endpoint`

Less helpful:

- `Stuff with config`
- `Need to look at proxy`

## Success criteria

You will know the system is working if, after returning to a project, you can answer these with minimal effort:

- What was I trying to accomplish?
- What has already been done?
- What are the unresolved questions?
- What should I do next?

If those answers are not easy to recover, tighten the checkpoint discipline or simplify the stored schema.
