import os
import sys
import subprocess
import re

def main():
    if len(sys.argv) < 2:
        print("Usage: python call.py <tool_name> [args...]")
        sys.exit(1)

    tool_name = sys.argv[1]
    tool_args = " ".join(sys.argv[2:])

    # Path to the agent's TOOLS.md
    tools_md_path = os.path.join(os.getcwd(), 'TOOLS.md')
    
    # Default env vars
    env_vars = {}
    
    # Try to extract variables from TOOLS.md
    if os.path.exists(tools_md_path):
        with open(tools_md_path, 'r') as f:
            content = f.read()
            
            # Pattern matching for CLICKUP_ keys and ENABLED_TOOLS
            patterns = [
                r'CLICKUP_API_KEY[:=]\s*([^\s\n]+)',
                r'CLICKUP_TEAM_ID[:=]\s*([^\s\n]+)',
                r'CLICKUP_MCP_LICENSE_KEY[:=]\s*([^\s\n]+)',
                r'ENABLED_TOOLS[:=]\s*([^\s\n]+)'
            ]
            
            for p in patterns:
                match = re.search(p, content)
                if match:
                    key = p.split('[:=]')[0]
                    env_vars[key] = match.group(1).strip()

    # Base command
    cmd = ['mcporter', 'call', '--stdio', 'npx -y @taazkareem/clickup-mcp-server']
    
    # Add env flags
    for k, v in env_vars.items():
        cmd.extend(['--env', f'{k}={v}'])
    
    # Add tool name
    cmd.append(tool_name)
    
    # Add tool args if any
    if tool_args:
        # Simple splitting of args for the subprocess call
        # In real usage, the agent might pass them as key=value
        import shlex
        cmd.extend(shlex.split(tool_args))

    print(f"Executing: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
        else:
            print(f"Error: {result.stderr}")
            sys.exit(result.returncode)
    except Exception as e:
        print(f"Execution failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
