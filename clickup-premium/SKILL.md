---
name: clickup-premium
description: "Advanced ClickUp integration for task management, time tracking, and document collaboration. Use when you need to: (1) Manage tasks, subtasks, and custom fields, (2) Track or log time, (3) Create or edit ClickUp Docs, (4) Communicate in chat channels. Trigger this skill to guide the user through credential configuration or to optimize complex ClickUp workflows."
---

# ClickUp MCP Premium

This skill enables deep integration with ClickUp using the premium MCP server. It is designed for multi-agent environments where different agents may require different credentials or tool sets.

## Setup & Multi-Agent Configuration

To support multiple agents with different workspaces or permissions, use the **Dynamic stdio Mode**. 

### 1. Agent-Specific Credentials (`TOOLS.md`)
Every agent using this skill must check their local `TOOLS.md` for the following:
- `CLICKUP_API_KEY`: The personal API key for this agent's account.
- `CLICKUP_TEAM_ID`: The specific workspace/team ID this agent should manage.
- `CLICKUP_MCP_LICENSE_KEY`: The premium license key.
- `ENABLED_TOOLS`: (Optional) A comma-separated list of tools to enable (e.g., `get_tasks,create_task`). Use this to minimize token overhead for specialized agents.

### 2. Calling the Tool Dynamically
If local credentials exist in `TOOLS.md`, the agent **must** use the `--stdio` and `--env` flags instead of a named server. This ensures "one-shot" isolation without needing to restart the gateway.

**Execution Pattern:**
```bash
mcporter call --stdio "npx -y @taazkareem/clickup-mcp-server" \
  --env CLICKUP_API_KEY=<FROM_TOOLS_MD> \
  --env CLICKUP_TEAM_ID=<FROM_TOOLS_MD> \
  --env CLICKUP_MCP_LICENSE_KEY=<FROM_TOOLS_MD> \
  --env ENABLED_TOOLS=<FROM_TOOLS_MD_OR_ROLE> \
  <TOOL_NAME> <ARGS>
```

### 3. Global Fallback
If no local credentials are found in `TOOLS.md`, use the global named server:
```bash
mcporter call ClickUp.<TOOL_NAME> <ARGS>
```

## Best Practices

### 1. Tool Minimization (`ENABLED_TOOLS`)
Specialized agents should only enable the tools they need.
- **Onboarding (Maya)**: `get_workspace_hierarchy,create_task,get_task`
- **Ops/PM (Alaric)**: `get_tasks,update_task,add_time_entry,create_task_comment`
- **Finance (Sterling)**: `get_tasks,get_task_comments` (for ROI analysis)

### 2. Hierarchy Discovery
Before creating tasks, use `get_workspace_hierarchy` to understand the structure of Spaces, Folders, and Lists.

### 3. Smart Task Lookup
The premium server supports automatic name resolution. You can provide a task **Name** directly to tools like `get_task` instead of searching for an ID first.

## Example Workflows

### Maya: Processing a New Lead
1. Read `TOOLS.md` for `CLICKUP_API_KEY`.
2. Discover Hierarchy to find the "Consulting" space.
3. Call `create_task` via `--stdio` with `ENABLED_TOOLS=create_task`.

### Alaric: Weekly Status Check
1. Read `TOOLS.md` for `CLICKUP_TEAM_ID`.
2. Call `get_tasks` via `--stdio` with `ENABLED_TOOLS=get_tasks,create_task_comment`.
3. Add comments to overdue tasks.
