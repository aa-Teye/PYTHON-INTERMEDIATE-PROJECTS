"""
PDF Scout v1.0
Author: Alex Teye Ametepey
Description: A simple tool to crawl a directory and find specific terms in PDFs.
Useful for scanning lecture notes or research papers quickly.
"""

import os
import sys
from PyPDF2 import PdfReader

def scout_files(target_dir, search_term):
    print(f"--- Scanning directory: {target_dir} ---")
    
    # Check if directory actually exists
    if not os.path.exists(target_dir):
        print(f"Error: The path '{target_dir}' is invalid.")
        return

    found_matches = 0
    
    # Loop through the files manually
    for file in os.listdir(target_dir):
        if file.endswith(".pdf"):
            full_path = os.path.join(target_dir, file)
            
            try:
                reader = PdfReader(full_path)
                # Loop through pages to find the text
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    content = page.extract_text()
                    
                    if search_term.lower() in content.lower():
                        print(f"[MATCH] Found '{search_term}' in {file} (Page {page_num + 1})")
                        found_matches += 1
            
            except Exception as e:
                # Common with corrupted PDFs or encrypted ones
                print(f"[SKIP] Could not read {file}: {e}")

    print(f"\n--- Scan Complete. Total matches found: {found_matches} ---")

if __name__ == "__main__":
    # If you want to run this from terminal directly
    if len(sys.argv) > 2:
        folder = sys.argv[1]
        term = sys.argv[2]
    else:
        # Fallback for VS Code Run button
        folder = input("Folder path to scan: ").strip()
        term = input("Keyword to search: ").strip()

    scout_files(folder, term)