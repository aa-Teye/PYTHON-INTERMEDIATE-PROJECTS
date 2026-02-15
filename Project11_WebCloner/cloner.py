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
    
    # Create structure
    for path in [domain, f"{domain}/data", f"{domain}/images"]:
        if not os.path.exists(path): os.makedirs(path)

    print(f"🕵️  Masking identity and connecting to {url}...")
    
    try:
        # Use the Browser Mask
        response = requests.get(url, headers=get_headers(), timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 1. LIVE ASSET TRACKING
        images = soup.find_all('img')
        print(f"📸 Found {len(images)} images. Starting download...")

        img_count = 0
        for img in images[:10]: # Limit to 10 for speed
            img_url = urljoin(url, img.get('src'))
            img_name = os.path.basename(urlparse(img_url).path)
            if not img_name: continue
            
            try:
                img_data = requests.get(img_url, headers=get_headers()).content
                with open(f"{domain}/images/{img_name}", "wb") as f:
                    f.write(img_data)
                img_count += 1
                print(f"   [{img_count}/{len(images[:10])}] Downloaded: {img_name}")
            except:
                continue

        # 2. FINAL REPORTING
        report = {
            "timestamp": time.ctime(),
            "target": url,
            "images_cloned": img_count,
            "security_headers": dict(response.headers)
        }

     