# install.ps1 — installs AI Context skills and initializes the global context store
$ErrorActionPreference = 'Stop'

$RepoDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$CollectionDir = Join-Path $RepoDir 'catalog\context-management'
$SkillsSrc = Join-Path $CollectionDir 'skills'
$SkillsDest = Join-Path $HOME '.copilot\skills'
$Script = Join-Path $SkillsDest 'context-tooling\scripts\contextctl.py'

$SkillDirs = @(
    'context-tooling'
    'context-resume'
    'context-checkpoint'
    'context-focus'
    'context-maintenance'
)

Write-Host "==> Creating skills directory: $SkillsDest"
New-Item -ItemType Directory -Force -Path $SkillsDest | Out-Null

Write-Host '==> Copying skills'
foreach ($skill in $SkillDirs) {
    $src = Join-Path $SkillsSrc $skill
    Copy-Item -Recurse -Force -Path $src -Destination $SkillsDest
    Write-Host "    Copied $skill"
}

Write-Host ''
Write-Host '==> Initialize first project'
$ProjectSlug = Read-Host 'Project slug (e.g. my-project)'
$input = Read-Host "Project title (e.g. My Project) [$ProjectSlug]"
$ProjectTitle = if ($input) { $input } else { $ProjectSlug }

python $Script init --project $ProjectSlug --title $ProjectTitle

Write-Host ''
Write-Host '==> Done.'
Write-Host ''
Write-Host 'Next step: create the Context Orchestrator custom agent in VS Code.'
Write-Host '  1. Open Copilot Chat'
Write-Host '  2. Open the agents dropdown'
Write-Host "  3. Choose 'Configure Custom Agents...'"
Write-Host '  4. Create a User profile agent'
Write-Host "  5. Paste the contents of: $CollectionDir\agents\context-orchestrator\context-orchestrator.agent.md"
Write-Host ''
Write-Host "Then try: @Context Orchestrator resume work on $ProjectSlug"
