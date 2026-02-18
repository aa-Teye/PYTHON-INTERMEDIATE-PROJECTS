# Project 10: GitHub API Supervisor

## 🛡️ Overview
This is an automated **Repository Auditor**. It uses the GitHub REST API to scan a specific repository, identify folders missing documentation (`README.md`), and provides an interactive terminal prompt to create and upload them automatically via Python.

## 🚀 Key Features
- **Remote Inspection:** Scans directories directly on the GitHub cloud.
- **Automated Repair:** Generates and pushes encoded files to the repository using `PUT` requests.
- **Base64 Integration:** Handles the binary-to-text encoding required by the GitHub Contents API.

## 🛠️ Technical Stack
- **Python 3.x**
- **Libraries:** `requests` (API communication), `base64` (data encoding).
- **GitHub REST API v3**

## 🚦 Usage Instructions
1. **Security:** Generate a Personal Access Token (PAT) from your GitHub settings.
2. **Configuration:** Update the `TOKEN`, `USERNAME`, and `REPO` variables in `supervisor.py`.
3. **Execution:** ```powershell
   python supervisor.py