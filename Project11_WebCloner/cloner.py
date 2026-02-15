import requests
from bs4 import BeautifulSoup
import os
import json
from urllib.parse import urljoin, urlparse

def upgrade_cloner():
    url = input("🕸️  Enter URL to Deep-Clone: ")
    domain = urlparse(url).netloc.replace('.', '_')
    
    # Setup Directory Structure
    paths = [domain, f"{domain}/images", f"{domain}/data"]
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)

    print(f"🚀 Starting Deep-Clone of {url}...")
    
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 1. THE DATA MAP (The DNA)
        manifest = {
            "source": url,
            "internal_links": [],
            "images_captured": []
        }

        # 2. Extract Links & Images
        for a in soup.find_all('a', href=True):
            link = urljoin(url, a['href'])
            if urlparse(url).netloc in link:
                manifest["internal_links"].append(link)

        # 3. Save HTML & Manifest
        with open(f"{domain}/index.html", "w", encoding="utf-8") as f:
            f.write(soup.prettify())
            
        with open(f"{domain}/data/manifest.json", "w") as f:
            json.dump(manifest, f, indent=4)

        print(f"✅ SUCCESS! Clone finished.")
        print(f"📂 Saved to: {domain}/")
        print(f"📊 Site Map created in: {domain}/data/manifest.json")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    upgrade_cloner()