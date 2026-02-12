import requests
import base64

# 🛡️ YOUR CREDENTIALS (Preserved)
TOKEN = "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"
USERNAME = "aa-Teye"
REPO = "PYTHON-INTERMEDIATE-PROJECTS"

def fix_missing_readme(folder_name, headers):
    """
    Asks the user for input and pushes a custom README.md to GitHub.
    """
    print(f"\n📢 ACTION REQUIRED: Missing documentation found in [{folder_name}]")
    
    # Capture your custom input
    user_desc = input(f"👉 Enter a description for this project: ")
    
    url = f"https://api.github.com/repos/{USERNAME}/{REPO}/contents/{folder_name}/README.md"
    
    # 🏗️ Constructing the professional file content
    content = f"# {folder_name}\n\n## Project Description\n{user_desc}\n\n---\n*Authored via Alex's Project 10: GitHub API Supervisor*"
    
    # API requires Base64 encoding
    encoded_content = base64.b64encode(content.encode()).decode()

    data = {
        "message": f"docs: user-generated README for {folder_name}",
        "content": encoded_content
    }

    # Use PUT to create the file
    response = requests.put(url, json=data, headers=headers)
    return response.status_code

def run_inspector():
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    url = f"https://api.github.com/repos/{USERNAME}/{REPO}/contents"
    
    print(f"\n{'='*60}")
    print(f"🛡️  DIGITAL SUPERVISOR: INSPECTING {REPO}")
    print(f"{'='*60}\n")
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"❌ Connection Error: {response.status_code}")
        return

    items = response.json()
    
    for item in items:
        # We only check directories (Project folders)
        if item['type'] == 'dir':
            folder_name = item['name']
            
            # Look inside the folder via the API
            folder_check = requests.get(item['url'], headers=headers)
            files_inside = [file['name'].lower() for file in folder_check.json()]
            
            # The Logic: Verify README presence
            if 'readme.md' in files_inside:
                print(f"✅ {folder_name:<35} | Status: DOCUMENTED")
            else:
                # 🛠️ Trigger the Interactive Repair
                status = fix_missing_readme(folder_name, headers)
                
                if status == 201:
                    print(f"   ✨ SUCCESS: README.md created on GitHub!")
                else:
                    print(f"   ❌ REPAIR FAILED: API Error {status}")

    print(f"\n{'='*60}")
    print(f"🎯 INSPECTION COMPLETE")
    print(f"{'='*60}")

if __name__ == "__main__":
    run_inspector()