# ClickUp Project Management Skill for OpenClaw

Natural language management of ClickUp workspaces via the [ClickUp MCP Server - Premium](https://github.com/taazkareem/clickup-mcp-server).

## Features

- **Tasks**: Create, update, move, duplicate, bulk operations, comments
- **Lists & Folders**: Full CRUD operations
- **Tags**: Create, manage, assign to tasks
- **Docs**: Create and manage pages
- **Time Tracking**: Start/stop timers, manual entries
- **Workspace**: Hierarchy, members, assignee resolution
- **Chat**: Channels and messaging

## Installation

```bash
openclaw skills install clickup-project-management
```

Or manually copy to `~/.openclaw/skills/clickup-project-management/`.

## Quick Start

1. Get a license key at [polar.sh/taazkareem](https://polar.sh/taazkareem)
2. Configure mcporter: `mcporter config add ClickUp https://clickup-mcp.taazkareem.com/mcp --auth oauth --header "X-License-Key=YOUR_KEY"`
3. Authenticate: `mcporter auth ClickUp`
4. Use: `mcporter call ClickUp.get_workspace_hierarchy`

## License

MIT
