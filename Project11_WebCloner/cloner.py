import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse

def is_internal(base_url, link_url):
    """Checks if a link belongs to the same website."""
    base_domain = urlparse(base_url).netloc
    link_domain = urlparse(link_url).netloc
    return link_domain == "" or link_domain == base_domain

def clone_recursive():
    url = input("🕸️ Enter URL for Recursive Crawl: ")
    domain_name = urlparse(url).netloc.replace('.', '_')
    
    if not os.path.exists(domain_name):
        os.makedirs(domain_name)

    print(f"🚀 Starting crawl on {url}...")
    
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 1. Save the Main Page
        with open(f"{domain_name}/index.html", "w", encoding="utf-8") as f:
            f.write(soup.prettify())

        # 2. THE RECURSIVE ENGINE: Find all internal links
        links = soup.find_all('a', href=True)
        internal_links = set() # Using a 'set' to avoid duplicates

        for link in links:
            href = link['href']
            full_url = urljoin(url, href)
            
            if is_internal(url, full_url):
                internal_links.add(full_url)

        print(f"🔗 Found {len(internal_links)} internal pages to crawl later.")
        for l in list(internal_links)[:5]: # Just show the first 5 for now
            print(f"   -> Found: {l}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    clone_recursive()