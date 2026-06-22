# Copilot Marketplace

Curated collections of GitHub Copilot agents and skills you can install into your user profile and compose for your workflow.

## Collections catalog

| Collection | Description | Items | Link |
| --- | --- | --- | --- |
| Context Management | Global, git-independent context continuity across sessions and repositories. | 1 agent, 5 skills | [catalog/context-management/README.md](catalog/context-management/README.md) |

## Browse and install

1. Choose a collection from the catalog and open its collection README.
2. Copy skill folders to `~/.copilot/skills` and add agent markdown files to your VS Code user-profile agents.
3. Follow any collection-specific setup guidance (for example bootstrap scripts and templates).

For the current Context Management collection, you can also use:

- Linux/macOS: `bash install.sh`
- Windows PowerShell: `.\install.ps1`

## Contributing new marketplace items

See [AGENTS.md](AGENTS.md) for repository conventions, required frontmatter, and checklists for adding items or new collections.

## Deep documentation

System-level architecture and operating guidance are in [docs/](docs/), starting with [docs/00-index.md](docs/00-index.md).
