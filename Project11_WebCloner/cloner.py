import requests
from bs4 import BeautifulSoup
import os
import json
import time
from urllib.parse import urljoin, urlparse

def get_headers():
    """Returns headers to mimic a real Chrome browser."""
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

def massive_cloner_v4():
    url = input("🕸️  Enter URL for Stealth Clone & Audit: ")
    domain = urlparse(url).netloc.replace('.', '_')
     