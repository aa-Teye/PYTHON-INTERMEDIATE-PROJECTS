import requests
import time
import csv
from datetime import datetime

# The list of sites you want to monitor
SITES = ["https://google.com", "https://github.com", "https://ug.edu.gh"]

def check_latency():
    print(f"--- NetWatcher Started at {datetime.now().strftime('%H:%M:%S')} ---")
    
    with open('latency_log.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # Write header only if file is empty
        if file.tell() == 0:
            writer.writerow(["Timestamp", "Site", "Latency (ms)", "Status"])

        for site in SITES:
            try:
                start_time = time.time()
                response = requests.get(site, timeout=5)
                end_time = time.time()
                
                # Calculate latency in milliseconds
                latency = round((end_time - start_time) * 1000, 2)
                status = "Online" if response.status_code == 200 else f"Error {response.status_code}"
                
                print(f"[{site}] {status} - {latency}ms")
                writer.writerow([datetime.now(), site, latency, status])
                
            except requests.exceptions.RequestException:
                print(f"[{site}] OFFLINE")
                writer.writerow([datetime.now(), site, "N/A", "Offline"])

if __name__ == "__main__":
    # For this project, we run it once, but you could wrap it in a loop!
    check_latency()