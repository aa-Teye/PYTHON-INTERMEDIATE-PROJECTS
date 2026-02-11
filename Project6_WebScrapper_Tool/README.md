# Project 06: Automated Web Scraper & CSV Generator 🕸️

## 📝 Overview
This repository contains an automated data extraction tool developed during my 2023 Python mastery push. The tool focuses on transforming unstructured web data into structured datasets for downstream analysis.

## 🚀 2023 Feature Focus
As of late 2023, this project adheres to **Python 3.12** standards, emphasizing:
* **Structural Pattern Matching**: Using `match-case` logic for handling HTTP status codes.
* **Enhanced f-strings**: Utilizing the refined f-string syntax introduced in the 3.12 release.
* **Type Safety**: Implementing Type Hinting for more robust and maintainable code.

## 🛠️ Tech Stack & Compatibility
* **Interpreter**: Python 3.11 / 3.12
* **Networking**: `requests` v2.31.0
* **Parsing**: `beautifulsoup4` v4.12.2
* **Output**: CSV (RFC 4180 compliant)



## 🔧 Installation (2023 Best Practices)
It is recommended to run this in a virtual environment to ensure dependency isolation:

1. Create the environment:
   ```powershell
   python -m venv venv

2.Activate it:
   .\venv\Scripts\Activate.ps1

3.Install dependencies:
pip install -r requirements.txt

4. Usage:
python scraper.py