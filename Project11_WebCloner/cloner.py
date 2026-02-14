import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse

def get_site_name(url):
    """Extracts a clean name from the URL to use as a folder name."""
    domain = urlparse(url).netloc
    return domain.replace('.', '_')

def clone_website():
    target_url = input("🔗 Enter the full URL to clone (e.g., https://example.com): ")
    
    try:
        # 1. Fetch the website content
        print(f"🕵️  Connecting to {target_url}...")
        response = requests.get(target_url, timeout=10)
        response.raise_for_status()
        
        # 2. Setup folders
        folder_name = get_site_name(target_url)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            os.makedirs(os.path.join(folder_name, "images"))
        
        # 3. Parse and Save HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        with open(os.path.join(folder_name, "index.html"), "w", encoding="utf-8") as f:
            f.write(soup.prettify())
        
        print(f"✅ HTML Saved! Look inside the '{folder_name}' folder.")
        
        # 4. Challenge: Download the first 5 images
        images = soup.find_all('img')
        print(f"📸 Found {len(images)} images. Cloning the first 5...")
        
        for img in images[:5]:
            img_url = urljoin(target_url, img.get('src'))
            img_name = os.path.basename(urlparse(img_url).path)
            if not img_name: continue
            
            img_data = requests.get(img_url).content
            with open(os.path.join(folder_name, "images", img_name), "wb") as f:
                f.write(img_data)
                print(f"   Downloaded: {img_name}")

    except Exception as e:
        print(f"❌ Error during cloning: {e}")

if __name__ == "__main__":
    clone_website()