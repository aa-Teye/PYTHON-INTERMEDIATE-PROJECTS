# Project 23: Automated File Organizer

## Overview
A system automation utility designed to manage directory clutter by sorting files into categorized sub-folders based on their file extensions. 

## Technical Features
- **Dynamic Categorization:** Maps file types to specific directories (Images, Documents, Videos, etc.).
- **Automatic Directory Provisioning:** Creates necessary sub-folders dynamically if they do not exist.
- **Robust File Handling:** Uses `shutil` for secure move operations across the file system.

## Execution
1. Run the script: `python organizer.py`
2. Provide a valid directory path (e.g., `C:\Users\Name\Downloads`).
3. The script will automatically scan and organize all recognized file types.