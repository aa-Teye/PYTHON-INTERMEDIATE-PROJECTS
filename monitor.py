"""
SitePulse v1.0
Author: Alex (Awonders)
Description: Automated tool to track website uptime.
"""

import requests
import csv
from datetime import datetime
import os

def check_sites(urls):
    results = []
    # Adding a header makes the request look like it's coming from a browser
    headers = {'User-Agent': 'Mozilla/5.0'}

    print(f"--- Status Check Started: {datetime.now()} ---")

    for url in urls:
        try:
            # 5-second timeout prevents the script from freezing on dead sites
            response = requests.get(url, headers=headers, timeout=5)
            status = response.status_code
            outcome = "ONLINE" if status == 200 else f"UNSTABLE ({status})"
        except Exception:
            status = "ERROR"
            outcome = "OFFLINE"

        print(f"[LOG] {url} is {outcome}")
        
        results.append({
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'url': url,
            'code': status,
            'outcome': outcome
        })
    return results

def log_results(data, file="health_log.csv"):
    is_new = not os.path.exists(file)
    with open(file, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['timestamp', 'url', 'code', 'outcome'])
        if is_new:
            writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    # List of sites to monitor
    targets = [
        "https://www.google.com",
        "https://www.ug.edu.gh", 
        "https://github.com",
        "https://this-should-fail-test.com"
    ]
    
