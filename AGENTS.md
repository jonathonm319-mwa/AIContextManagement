# AGENTS.md

This file defines marketplace conventions for adding and maintaining Copilot agents and skills in this repository.

## Repository conventions

- Place all marketplace content under `catalog/<collection-slug>/`.
- Use lowercase kebab-case for collection and skill folder names.
- Place agents under `catalog/<collection-slug>/agents/<agent-slug>/`.
- Place skills under `catalog/<collection-slug>/skills/<skill-slug>/`.
- Each collection must include `catalog/<collection-slug>/README.md`.

### Required files per item

- **Skill**: `SKILL.md` (with frontmatter + usage instructions)
- **Agent**: `<name>.agent.md` (with frontmatter + behavior instructions)

## Collection rules

Create a **new collection** when items serve a distinct use case, audience, or workflow.
Add to an **existing collection** when the new item directly extends that collection’s workflow and shared context.
Group related agents and skills so users can discover and install cohesive sets.

## Checklist: adding a new item

- [ ] Choose target collection under `catalog/`.
- [ ] Add item folder in the correct `agents/` or `skills/` path.
- [ ] Include required markdown file (`.agent.md` or `SKILL.md`) with valid frontmatter.
- [ ] Update that collection’s `README.md` to mention the new item.
- [ ] Update root `README.md` catalog counts/description if needed.
- [ ] Update `install.sh` and `install.ps1` if bootstrap behavior should include the new item.

## Checklist: adding a new collection

- [ ] Create `catalog/<collection-slug>/`.
- [ ] Add `README.md` with purpose, item relationships, install guidance, and prompt examples.
- [ ] Add `agents/` and/or `skills/` subfolders and item files.
- [ ] Add collection row to root `README.md` catalog table.
- [ ] Decide whether install scripts should support this collection now or remain focused on an existing default.

## Collection README template

At minimum include:

1. What the collection does
2. Who/when it is for
3. Relationship between included agents and skills
4. Installation steps
5. Suggested prompts

## Frontmatter reference

### Skill frontmatter

Required:

- `name`
- `description`

Optional:

- Additional metadata fields as supported by Copilot skills

### Agent frontmatter

Required:

- `name`
- `description`
- `target`
- `user-invocable`
- `disable-model-invocation`

Optional:

- Additional metadata fields as supported by custom agents
