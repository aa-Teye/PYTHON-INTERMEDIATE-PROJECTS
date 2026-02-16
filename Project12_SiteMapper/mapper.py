import requests
from bs4 import BeautifulSoup
import json
import xml.etree.ElementTree as ET
from urllib.parse import urljoin, urlparse
from datetime import datetime

class SiteMapper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.domain = urlparse(base_url).netloc
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'}
        self.map_data = {
            "metadata": {
                "root": base_url,
                "scan_time": str(datetime.now()),
                "domain": self.domain
            },
            "internal_endpoints": [],
            "external_references": []
        }

    def generate_map(self):
        print(f"Scanning directory structure for: {self.domain}")
        try:
            response = requests.get(self.base_url, headers=self.headers, timeout=15)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            for link in soup.find_all('a', href=True):
                full_url = urljoin(self.base_url, link['href'])
                
                if self.domain in full_url:
                    if full_url not in self.map_data["internal_endpoints"]:
                        self.map_data["internal_endpoints"].append(full_url)
                else:
                    if full_url not in self.map_data["external_references"]:
                        self.map_data["external_references"].append(full_url)

            self.export_data()

        except Exception as e:
            print(f"Mapping Failure: {str(e)}")

    def export_data(self):
        # Export as JSON
        with open("sitemap.json", "w") as f:
            json.dump(self.map_data, f, indent=4)
        
        print("Export complete: sitemap.json generated.")

if __name__ == "__main__":
    target = input("Enter target URL for mapping: ").strip()
    mapper = SiteMapper(target)
    mapper.generate_map()