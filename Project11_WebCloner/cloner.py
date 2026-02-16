import requests
from bs4 import BeautifulSoup
import os
import json
import time
import re
from urllib.parse import urljoin, urlparse

def get_headers():
    """Returns headers to mimic a standard Chrome browser session."""
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

def sanitize_filename(filename):
    """Removes invalid characters and query strings for OS compatibility."""
    # Remove query strings (anything after ?)
    base_name = filename.split('?')[0]
    # Remove characters not allowed in Windows/Linux filenames
    return re.sub(r'[\\/*?:"<>|]', "", base_name)

def massive_cloner_v5():
    url = input("Enter target URL for cloning and audit: ").strip()
    
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        print("Error: Invalid URL. Protocol (http/https) is required.")
        return
        
    domain = parsed_url.netloc.replace('.', '_')
    
    # Directory initialization
    directories = [domain, f"{domain}/data", f"{domain}/images"]
    for path in directories:
        os.makedirs(path, exist_ok=True)

    print(f"Initializing connection to {url}...")
    
    try:
        session = requests.Session()
        response = session.get(url, headers=get_headers(), timeout=15)
        response.raise_for_status()
        
        # Detect actual encoding to prevent character corruption
        content_encoding = response.encoding if response.encoding else 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        images = soup.find_all('img')
        print(f"Metadata analysis: {len(images)} assets identified.")

        img_count = 0
        target_limit = 10 
        
        for img in images[:target_limit]:
            src = img.get('src')
            if not src or src.startswith('data:'): # Skip Base64 encoded images
                continue
                
            img_url = urljoin(url, src)
            
            # Extract and sanitize filename
            raw_name = os.path.basename(urlparse(img_url).path)
            img_name = sanitize_filename(raw_name) if raw_name else f"asset_{img_count}.jpg"
            
            try:
                img_response = session.get(img_url, headers=get_headers(), timeout=10)
                img_response.raise_for_status()
                
                file_path = os.path.join(domain, "images", img_name)
                with open(file_path, "wb") as f:
                    f.write(img_response.content)
                
                img_count += 1
                print(f"Buffered asset [{img_count}/{target_limit}]: {img_name}")
            except Exception as e:
                print(f"Sync error for {img_name}: {str(e)}")
                continue

        # Technical Report Generation
        report_data = {
            "timestamp": time.ctime(),
            "target": url,
            "encoding_detected": content_encoding,
            "assets_cloned": img_count,
            "server_headers": dict(response.headers)
        }

        # Save HTML using detected encoding
        with open(f"{domain}/index.html", "w", encoding=content_encoding) as f:
            f.write(soup.prettify())
            
        with open(f"{domain}/data/audit_manifest.json", "w") as f:
            json.dump(report_data, f, indent=4)

        print("\nSession Finalized.")
        print(f"Directory: {domain}/")
        print(f"Audit Log: {domain}/data/audit_manifest.json")

    except requests.exceptions.RequestException as e:
        print(f"Network Layer Error: {e}")
    except Exception as e:
        print(f"Application Layer Error: {e}")

if __name__ == "__main__":
    massive_cloner_v5()