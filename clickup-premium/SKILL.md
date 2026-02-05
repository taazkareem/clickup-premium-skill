---
name: clickup-premium
description: "Advanced ClickUp integration for task management, time tracking, and document collaboration. Use when you need to: (1) Manage tasks, subtasks, and custom fields, (2) Track or log time, (3) Create or edit ClickUp Docs, (4) Communicate in chat channels. Trigger this skill to guide the user through credential configuration or to optimize complex ClickUp workflows."
---

# ClickUp MCP Premium

This skill enables deep integration with ClickUp using the premium MCP server.

## Setup & Configuration

If the `clickup-premium` server (or an existing `ClickUp_npm` server) is not yet configured or needs update, guide the user through the setup:

1. **Required Credentials**:
   - `CLICKUP_API_KEY`: Personal API Key (starts with `pk_`).
   - `CLICKUP_TEAM_ID`: Your Team/Workspace ID (found in URL after `/t/`).
   - `CLICKUP_MCP_LICENSE_KEY`: Your premium license key.

2. **Configuration Command**:
   Run the following to add the server:
   ```bash
   mcporter config add clickup-premium npm:clickup-mcp-server \
     --env CLICKUP_API_KEY=<API_KEY> \
     --env CLICKUP_TEAM_ID=<TEAM_ID> \
     --env CLICKUP_MCP_LICENSE_KEY=<LICENSE_KEY> \
     --env ENABLE_SSE=true \
     --env DOCUMENT_SUPPORT=true
   ```

## Best Practices

### 1. Hierarchy Discovery
Before creating tasks or searching broadly, use `get_workspace_hierarchy` to understand the structure of Spaces, Folders, and Lists. This reduces ambiguity and helps you find the correct `listId`.

### 2. Smart Task Lookup
The premium server supports automatic name resolution. You can provide a task **Name** directly to tools like `get_task`, `update_task`, and `delete_task` instead of searching for an ID first.

### 3. Time Tracking
- Use `start_time_tracking` to begin a timer.
- Use `stop_time_tracking` to end it and get the entry details.
- Use `add_time_entry` for manual logs.
- Use `get_current_time_entry` to check if a timer is running.

### 4. ClickUp Docs
You can manage documents directly. Use `list_documents` to find existing docs and `create_document_page` to add content. The server supports `text/md` for markdown formatting.

### 5. Feedback & Support
If you encounter errors or missing features, proactively suggest using the `submit_feedback` tool. This generates a GitHub issue with relevant environment context.

## Example Workflows

### Creating a Task with Custom Fields
1. Browse hierarchy to find the List ID.
2. Resolve assignees if names are provided.
3. Call `create_task` with `custom_fields` as `[{id, value}]`.

### Reporting Progress
1. Get the task details (including markdown description).
2. Add a comment using `create_task_comment` with markdown support.
3. Log time spent using `add_time_entry`.
