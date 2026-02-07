import os
import subprocess
import json
import sys

def main():
    print("🚀 Initializing ClickUp MCP Premium Skill...")
    
    # 1. Check for mcporter
    try:
        subprocess.run(["mcporter", "--version"], capture_output=True, check=True)
        print("✅ mcporter detected.")
    except Exception:
        print("❌ Error: mcporter is not installed. This is a prerequisite for this skill.")
        sys.exit(1)

    # 2. Check for credentials
    required = ['CLICKUP_API_KEY', 'CLICKUP_TEAM_ID', 'CLICKUP_MCP_LICENSE_KEY']
    missing = [k for k in required if not os.getenv(k) and not os.path.exists('.clickup-auth')]
    
    if missing:
        print(f"⚠️ Warning: Missing environment variables: {', '.join(missing)}")
        print("   Please set these in your environment or create a .clickup-auth file.")
    else:
        print("✅ Credentials detected.")

    print("\nSkill is ready for use via scripts/call.py.")

if __name__ == "__main__":
    main()
