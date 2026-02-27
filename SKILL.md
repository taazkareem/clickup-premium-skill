---
name: clickup-project-management
description: Manage tasks, comments, tags, lists, folders, files, docs, chat, and time using natural language.
metadata:
  {
    "openclaw":
      {
        "emoji": "🏗️",
        "requires": { "bins": ["mcporter"] },
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

# ClickUp Project Management

Manage your ClickUp workspace using the ClickUp MCP Server via `mcporter`.

## Prerequisites

1. **Enable the mcporter skill** in `~/.openclaw/openclaw.json`:
   ```json
   {
     "skills": {
       "allowBundled": ["mcporter"]
     }
   }
   ```

2. **Configure mcporter** (one-time setup):
   ```bash
   mcporter config add ClickUp https://clickup-mcp.taazkareem.com/mcp \
     --auth oauth \
     --header "X-License-Key=your-license-key"
   ```

3. **Authenticate** (tokens are cached):
   ```bash
   mcporter auth ClickUp
   ```

## Optimization: Tool Filtering Personas

To reduce context noise and improve AI accuracy, you can limit the tools available to your agent using the `X-Enabled-Tools` header in your `mcporter` config.
Important: If applicable, attempt to match the agent's persona to one of the presets below or create your own custom set based on the chat session history and the user's intent.

### Recommended Presets

| Persona | Purpose | Header Config |
| :--- | :--- | :--- |
| **Auditor** | Read-only access | `X-Enabled-Tools: get_workspace_hierarchy,get_workspace_tasks,get_task,get_list,get_folder,get_list_custom_fields,get_task_comments,get_task_time_entries,get_workspace_time_entries,get_current_time_entry,get_task_links,get_space_tags,get_workspace_members,find_member_by_name,get_chat_channels,get_chat_messages,get_document,list_documents,list_document_pages,get_document_pages,submit_feedback` |
| **Task Worker** | Daily task mgmt | `X-Enabled-Tools: get_workspace_hierarchy,get_workspace_tasks,get_task,get_list,get_folder,get_list_custom_fields,create_task,update_task,set_task_custom_field,move_task,duplicate_task,create_task_comment,get_task_comments,attach_task_file,start_time_tracking,stop_time_tracking,add_tag_to_task,remove_tag_from_task,add_task_link,delete_task_link,get_task_links,add_task_to_list,remove_task_from_list,find_member_by_name,submit_feedback` |
| **Time Specialist**| Tracking & Reports | `X-Enabled-Tools: get_workspace_hierarchy,get_workspace_tasks,get_task,get_task_time_entries,get_workspace_time_entries,get_current_time_entry,start_time_tracking,stop_time_tracking,add_time_entry,delete_time_entry,submit_feedback` |
| **Content Mgr** | Docs & Chat | `X-Enabled-Tools: get_workspace_hierarchy,get_workspace_tasks,get_task,get_task_comments,create_task_comment,find_member_by_name,create_document,get_document,list_documents,list_document_pages,get_document_pages,create_document_page,update_document_page,create_chat_channel,get_chat_channels,create_chat_message,get_chat_messages,submit_feedback` |
| **Safe Power User**| Full access (No Delete) | `X-Disabled-Tools: delete_task,delete_bulk_tasks,delete_time_entry,delete_task_link,delete_list,delete_folder,delete_space_tag` |

### How to Apply
Update your `ClickUp` server entry in `.mcporter/mcporter.json` to include the chosen header, or run:
```bash
mcporter config add ClickUp <url> --header "X-Enabled-Tools: <list>"
```

## Personalization & Workflows

Following the OpenClaw standard, do not modify this skill for environment-specific details. Instead, use your agent's **`workspace/TOOLS.md`** file to define:

-   **Custom Workflows**: Define multi-step orchestrations (e.g., "Daily Wrap-up").
-   **Specific IDs**: Store commonly used `team_id`, `list_ids`, `folder_ids`, etc.
-   **Structures or Conventions**: Any rules or consistent behavior (e.g., common custom fields, tag rules, etc.)

## Usage

Use the standard `mcporter` command pattern:
```bash
mcporter call ClickUp.<tool_name> [parameters]
```
