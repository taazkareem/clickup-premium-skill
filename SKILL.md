---
name: clickup-premium
description: "Advanced ClickUp integration for task management, time tracking, and document collaboration. Use when you need to: (1) Manage tasks, subtasks, and custom fields, (2) Track or log time, (3) Create or edit ClickUp Docs, (4) Communicate in chat channels. Trigger this skill to guide the user through credential configuration or to optimize complex ClickUp workflows."
---

# ClickUp MCP Premium

This skill enables deep integration with ClickUp using the premium MCP server. It is optimized for multi-agent environments using a **Dynamic stdio Mode** that ensures credential isolation.

## Setup & Multi-Agent Configuration

### 1. Agent-Specific Credentials (`TOOLS.md`)
Every agent using this skill should have its specific credentials stored in its local `TOOLS.md` file:
- `CLICKUP_API_KEY`: Personal API Key.
- `CLICKUP_TEAM_ID`: The specific workspace/team ID.
- `CLICKUP_MCP_LICENSE_KEY`: The premium license key.
- `ENABLED_TOOLS`: (Optional) Comma-separated list of tools to enable.

### 2. Calling Tools (The Launcher)
To ensure isolation and proper environment loading, **ALWAYS** use the included launcher script. This script automatically reads your `TOOLS.md` and injects the variables into a one-shot `mcporter` session.

**Usage Pattern:**
```bash
python <skill_path>/scripts/call.py <TOOL_NAME> [ARGS]
```

**Example:**
```bash
python /Users/admin/.openclaw/skills/clickup-premium/scripts/call.py get_tasks teamId=9013667057
```

## Best Practices

### 1. Hierarchy Discovery
Before creating tasks, use `get_workspace_hierarchy` via the launcher to understand the structure of Spaces and Folders.

### 2. Smart Task Lookup
The premium server supports automatic name resolution. You can provide a task **Name** directly to tools instead of searching for a numeric ID first.

### 3. Tool Minimization (`ENABLED_TOOLS`)
Specialized agents should list only required tools in their `TOOLS.md` to minimize token overhead and increase reliability.

## Example Workflows

### Maya: Processing a New Lead
1. Run `python <skill_path>/scripts/call.py create_task listId=... name="New Client"`
2. The script handles the `npx` spawn and `TOOLS.md` parsing automatically.

### Alaric: Status Update
1. Run `python <skill_path>/scripts/call.py create_task_comment taskId=... comment="Task in progress"`
