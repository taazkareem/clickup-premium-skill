---
name: clickup-project-management
description: "Professional-grade ClickUp orchestration for task automation, workspace hierarchy management, and team collaboration. Features auto-scoping and remote-first execution."
metadata:
  {
    "openclaw":
      {
        "emoji": "🏗️",
        "requires": { "bins": ["mcporter", "python3"] },
        "install":
          [
            {
              "id": "node",
              "kind": "node",
              "package": "mcporter",
              "bins": ["mcporter"],
              "label": "Install mcporter",
            },
          ],
      },
  }
---

# ClickUp Project Management Skill

This skill provides a high-performance interface for managing ClickUp tasks, lists, and folders. It is designed to be **context-aware**, automatically pulling `CLICKUP_TEAM_ID` and `CLICKUP_OPERATIONS_LIST_ID` from your `TOOLS.md` if available.

## Design Philosophy

This skill is a **Tool Library**. It focuses on providing reliable access to the ClickUp API. Business-specific SOPs (e.g., "How we name our projects") should be defined in your `SOUL.md` or `AGENTS.md`.

## Tool Reference

Use the bundled launcher to execute tools. This ensures proper authentication and automatic fallback between remote (fast) and local (fallback) execution.

**Usage:** `python {baseDir}/scripts/call.py <TOOL_NAME> [ARGS]`

### 1. Task Management
- `get_tasks`: List tasks in a list/folder.
- `create_task`: Create a new task (name, description, status).
- `update_task`: Modify existing tasks.
- `add_task_comment`: Post updates to a task.

### 2. Hierarchy & Structure
- `get_workspace_hierarchy`: See all Spaces, Folders, and Lists.
- `create_folder`: Organize your project workspace.
- `create_list`: Create lists within folders or spaces.

### 3. Intelligence & Analytics
- `get_task_details`: Get full metadata for a specific task.
- `get_list_details`: Inspect list-level configurations.

## Automatic Scoping
The launcher automatically checks your local `TOOLS.md` for the following keys:
- `CLICKUP_TEAM_ID`: Used as default `teamId`.
- `CLICKUP_OPERATIONS_LIST_ID`: Used as default `listId`.

This allows you to simply say "Create a task called Finish Report" without having to provide IDs every time.

## Configuration
Requires `CLICKUP_API_KEY` to be set in your `openclaw.json` or process environment.
