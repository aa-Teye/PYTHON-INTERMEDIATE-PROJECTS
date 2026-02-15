import requests
from bs4 import BeautifulSoup
import os
import json
from urllib.parse import urljoin, urlparse

def get_metadata(soup):
    """Extracts SEO and site metadata."""
    return {
        "title": soup.title.string if soup.title else "No Title",
        "description": soup.find("meta", attrs={"name": "description"})["content"] if soup.find("meta", attrs={"name": "description"}) else "No Description",
        "keywords": soup.find("meta", attrs={"name": "keywords"})["content"] if soup.find("meta", attrs={"name": "keywords"}) else "No Keywords"
    }

def analyze_security(headers):
    """Checks for common security headers."""
    security_checks = ["Content-Security-Policy", "Strict-Transport-Security", "X-Frame-Options"]
    return {header: ("Protected" if header in headers else "Missing") for header in security_checks}

def massive_cloner_v3():
    url = input("🕸️  Enter URL for Massive Analysis & Clone: ")
    domain = urlparse(url).netloc.replace('.', '_')
    
    # Setup Folders
    for path in [domain, f"{domain}/data"]:
        if not os.path.exists(path): os.makedirs(path)

    print(f"🚀 Analyzing and Cloning {url}...")
    
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 1. Advanced Data Mapping
        manifest = {
            "url": url,
            "metadata": get_metadata(soup),
            "security_score": analyze_security(response.headers),
            "links_found": [urljoin(url, a['href']) for a in soup.find_all('a', href=True)][:20] # Top 20 links
        }

        # 2. Save the Mirror
        with open(f"{domain}/index.html", "w", encoding="utf-8") as f:
            f.write(soup.prettify())
            
        # 3. Save the Intelligence Report
        with open(f"{domain}/data/audit_report.json", "w") as f:
            json.dump(manifest, f, indent=4)

        print(f"✅ DONE! Site cloned and Security Audit saved to {domain}/data/audit_report.json")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    massive_cloner_v3()