# Overview

## Purpose

This setup exists to preserve **working momentum** across sessions, projects, and repositories.

The core problem is that task switching and interruptions create restart friction. By saving a structured checkpoint of the current work state, an AI agent can help reconstruct:

- what the user was doing
- what is already true
- what still needs attention
- what the next best actions are

## Desired outcomes

The system is intentionally designed to optimize for:

1. **Fast re-entry** after interruption
2. **Cross-repository continuity** without storing task state in git repos
3. **Actionable summaries** instead of raw transcripts
4. **Reusable workflows** that can be used in many workspaces
5. **Separation of static guidance from dynamic state**

## High-level approach

The solution combines three layers:

1. **Custom agent** — provides a persistent persona and orchestration behavior
2. **Skills** — provide reusable task-specific capabilities such as resume, checkpoint, focus, and maintenance
3. **External context store** — provides a global, non-repository source of truth for active work state

## Why this matters

The system is not trying to remember everything. It is trying to preserve the minimum set of information needed to:

- restart quickly
- avoid repeating the same analysis
- maintain continuity across multiple domains of work
- reduce the cognitive load of context switching
