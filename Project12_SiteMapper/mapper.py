import requests
from bs4 import BeautifulSoup
import json
import xml.etree.ElementTree as ET
from urllib.parse import urljoin, urlparse
from datetime import datetime
import time
from concurrent.futures import ThreadPoolExecutor

class SiteMapperFinal:
    def __init__(self, base_url, max_pages=50):
        self.base_url = base_url.rstrip('/')
        self.domain = urlparse(base_url).netloc
        self.max_pages = max_pages
        self.to_visit = [self.base_url]
        self.visited = {}  # URL: Status Code
        self.external_links = set()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'}

    def process_url(self, url):
        """Fetches a URL and extracts all links."""
        if len(self.visited) >= self.max_pages or url in self.visited:
            return

        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            self.visited[url] = response.status_code
            
            if response.status_code != 200:
                return []

            soup = BeautifulSoup(response.text, 'html.parser')
            discovered = []

            for link in soup.find_all('a', href=True):
                full_url = urljoin(self.base_url, link['href']).split('#')[0].rstrip('/')
                
                if urlparse(full_url).netloc == self.domain:
                    discovered.append(full_url)
                else:
                    self.external_links.add(full_url)
            
            return discovered

        except Exception as e:
            self.visited[url] = "Error"
            return []

    def run_concurrent_map(self):
        """Uses ThreadPoolExecutor to map the site rapidly."""
        print(f"Initializing concurrent audit for: {self.domain}")
        
        while self.to_visit and len(self.visited) < self.max_pages:
            current_batch = self.to_visit[:5]  # Process 5 at a time
            self.to_visit = self.to_visit[5:]

            with ThreadPoolExecutor(max_workers=5) as executor:
                results = executor.map(self.process_url, current_batch)
                
                for discovered_links in results:
                    if discovered_links:
                        for link in discovered_links:
                            if link not in self.visited and link not in self.to_visit:
                                self.to_visit.append(link)

    def export_reports(self):
        """Saves detailed technical manifests."""
        # JSON Detailed Audit
        report = {
            "metadata": {
                "root": self.base_url,
                "timestamp": str(datetime.now()),
                "pages_crawled": len(self.visited),
                "external_refs": len(self.external_links)
            },
            "internal_inventory": self.visited,
            "external_inventory": list(self.external_links)
        }
        
        with open("site_audit.json", "w") as f:
            json.dump(report, f, indent=4)
        
        print(f"Technical Audit saved: site_audit.json")

if __name__ == "__main__":
    target = input("Enter target URL for technical audit: ").strip()
    mapper = SiteMapperFinal(target)
    
    start = time.time()
    mapper.run_concurrent_map()
    mapper.export_reports()
    
    print(f"\nAudit completed in {round(time.time() - start, 2)} seconds.")