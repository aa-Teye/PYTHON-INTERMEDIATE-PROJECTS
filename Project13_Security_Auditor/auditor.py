import requests
import time
import json
from datetime import datetime

class SecurityAuditor:
    def __init__(self, target_url):
        self.url = target_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'
        }
        self.results = {}

    def run_audit(self):
        print(f"Starting performance and security audit for: {self.url}")
        
        try:
            # Measure Latency
            start_time = time.time()
            response = requests.get(self.url, headers=self.headers, timeout=15)
            end_time = time.time()
            
            latency = round((end_time - start_time) * 1000, 2) # Convert to ms
            
            # Security Headers to check
            security_headers = [
                "Content-Security-Policy",
                "Strict-Transport-Security",
                "X-Content-Type-Options",
                "X-Frame-Options",
                "X-XSS-Protection"
            ]
            
            found_headers = {h: response.headers.get(h, "MISSING") for h in security_headers}
            
            self.results = {
                "audit_time": str(datetime.now()),
                "target": self.url,
                "performance": {
                    "latency_ms": latency,
                    "status_code": response.status_code
                },
                "security_headers": found_headers
            }
            
            self.save_report()

        except Exception as e:
            print(f"Audit failed: {str(e)}")

    def save_report(self):
        with open("audit_report.json", "w") as f:
            json.dump(self.results, f, indent=4)
        print("Audit complete. Report saved to audit_report.json")

if __name__ == "__main__":
    target = input("Enter target URL for security audit: ").strip()
    auditor = SecurityAuditor(target)
    auditor.run_audit()