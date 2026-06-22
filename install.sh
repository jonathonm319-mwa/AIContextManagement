#!/usr/bin/env bash
# install.sh — installs AI Context skills and initializes the global context store
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COLLECTION_DIR="$REPO_DIR/catalog/context-management"
SKILLS_SRC="$COLLECTION_DIR/skills"
SKILLS_DEST="$HOME/.copilot/skills"
SCRIPT="$SKILLS_DEST/context-tooling/scripts/contextctl.py"

SKILL_DIRS=(
  context-tooling
  context-resume
  context-checkpoint
  context-focus
  context-maintenance
)

echo "==> Creating skills directory: $SKILLS_DEST"
mkdir -p "$SKILLS_DEST"

echo "==> Copying skills"
for skill in "${SKILL_DIRS[@]}"; do
  cp -r "$SKILLS_SRC/$skill" "$SKILLS_DEST/"
  echo "    Copied $skill"
done

echo ""
echo "==> Initialize first project"
read -rp "Project slug (e.g. my-project): " PROJECT_SLUG
read -rp "Project title (e.g. My Project) [${PROJECT_SLUG}]: " PROJECT_TITLE
PROJECT_TITLE="${PROJECT_TITLE:-$PROJECT_SLUG}"

python "$SCRIPT" init --project "$PROJECT_SLUG" --title "$PROJECT_TITLE"

echo ""
echo "==> Done."
echo ""
echo "Next step: create the Context Orchestrator custom agent in VS Code."
echo "  1. Open Copilot Chat"
echo "  2. Open the agents dropdown"
echo "  3. Choose 'Configure Custom Agents...'"
echo "  4. Create a User profile agent"
echo "  5. Paste the contents of: $COLLECTION_DIR/agents/context-orchestrator/context-orchestrator.agent.md"
echo ""
echo "Then try: @Context Orchestrator resume work on $PROJECT_SLUG"
