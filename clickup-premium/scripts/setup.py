import os
import subprocess
import json
import sys

def run_mcporter(cmd):
    try:
        result = subprocess.run(f"mcporter {cmd}", shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return None

def main():
    print("Checking ClickUp MCP Premium configuration...")
    
    # Check if clickup-premium or ClickUp_npm exists
    config_list = run_mcporter("config list --json")
    if not config_list:
        print("Error: Could not list mcporter config.")
        sys.exit(1)
        
    configs = json.loads(config_list)
    clickup_config = next((c for c in configs if c['name'] in ['clickup-premium', 'ClickUp_npm']), None)
    
    if not clickup_config:
        print("ClickUp MCP server not found in mcporter config.")
        print("Please follow the setup instructions in SKILL.md.")
        sys.exit(0)
        
    print(f"Found configuration: {clickup_config['name']}")
    
    # Check for required env vars
    env = clickup_config.get('env', {})
    required = ['CLICKUP_API_KEY', 'CLICKUP_TEAM_ID', 'CLICKUP_MCP_LICENSE_KEY']
    missing = [k for k in required if k not in env]
    
    if missing:
        print(f"Missing environment variables: {', '.join(missing)}")
    else:
        print("All required environment variables are present.")
        
    # Attempt a simple tool call to verify
    print("Testing connection...")
    test_result = run_mcporter(f"call {clickup_config['name']} get_workspace_members")
    if test_result and "error" not in test_result.lower():
        print("Connection successful!")
    else:
        print("Connection failed. Please check your credentials and license key.")

if __name__ == "__main__":
    main()
