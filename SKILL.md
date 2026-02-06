---
name: clickup-premium
description: "Advanced ClickUp integration for task management, time tracking, and document collaboration. Use when you need to: (1) Manage tasks, subtasks, and custom fields, (2) Track or log time, (3) Create or edit ClickUp Docs, (4) Communicate in chat channels. Trigger this skill to guide the user through credential configuration or to optimize complex ClickUp workflows."
---

# ClickUp MCP Premium

This skill enables deep integration with ClickUp using the premium MCP server. It supports both standalone usage and multi-agent environments where different agents require isolated credentials.

## Setup & Configuration

### 1. Simple Configuration (Standalone)
If you are the only user of this skill, add the server globally:
```bash
mcporter config add clickup-premium npm:clickup-mcp-server \
  --env CLICKUP_API_KEY=<YOUR_API_KEY> \
  --env CLICKUP_TEAM_ID=<YOUR_TEAM_ID> \
  --env CLICKUP_MCP_LICENSE_KEY=<YOUR_LICENSE_KEY>
```
Then call tools using: `mcporter call clickup-premium.get_tasks`

### 2. Multi-Agent Configuration (Isolated)
To support multiple agents with different permissions, use **Dynamic Mode**. 

**Required Credentials (`TOOLS.md` or Environment):**
- `CLICKUP_API_KEY`: Personal API Key.
- `CLICKUP_TEAM_ID`: The specific workspace ID.
- `CLICKUP_MCP_LICENSE_KEY`: The premium license key.
- `ENABLED_TOOLS`: (Optional) Comma-separated list of tools to enable (e.g., `get_tasks,create_task`) to minimize token overhead.

**Dynamic Call Pattern:**
```bash
mcporter call --stdio "npx -y @taazkareem/clickup-mcp-server" \
  --env CLICKUP_API_KEY=<API_KEY> \
  --env CLICKUP_TEAM_ID=<TEAM_ID> \
  --env CLICKUP_MCP_LICENSE_KEY=<LICENSE_KEY> \
  --env ENABLED_TOOLS=<ENABLED_TOOLS> \
  <TOOL_NAME> <ARGS>
```

## Best Practices

### 1. Hierarchy Discovery
Before creating tasks, use `get_workspace_hierarchy` to understand the structure of Spaces and Folders. This ensures you are targeting the correct `listId`.

### 2. Smart Task Lookup
The premium server supports automatic name resolution. You can provide a task **Name** directly to tools like `get_task` or `update_task` instead of searching for a numeric ID first.

### 3. Tool Minimization
When spawning specialized sub-agents, use the `ENABLED_TOOLS` environment variable to expose only the tools necessary for their specific role (e.g., only "Time Tracking" for an operations agent).

## Example Workflows

### Processing a Task
1. Get task details (returns markdown description).
2. Add a progress comment using `create_task_comment`.
3. Log time spent using `add_time_entry`.
