# Project 11: Massive Website Cloner (Spider Edition) 🕸️

## 📂 Overview
A professional-grade web crawler that mirrors website content. Unlike basic downloaders, this version includes a "Spider Engine" that identifies internal links to map out entire website structures.

## 🛠️ Tech Stack
- **Python 3**
- **Requests**: For robust HTTP connection handling.
- **BeautifulSoup4**: For DOM parsing and link extraction.
- **urllib.parse**: For sophisticated URL validation and domain filtering.

## 🚀 Features
- [x] **Recursive Link Detection**: Automatically identifies internal URLs vs. external links.
- [x] **Smart Folder Manlementation of automated multi-page downloading.

## 📝 Usage
1. Run `python cloner.py`.
2. Input the target URL.
3. The spider will scan the page and list all internal sub-pages discovered.