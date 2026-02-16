import psutil
import time
import platform
from datetime import datetime

class SystemPulse:
    def __init__(self, cpu_limit=80, ram_limit=85):
        self.cpu_limit = cpu_limit
        self.ram_limit = ram_limit
        self.os_info = platform.system()

    def check_vitals(self):
        # Get live hardware data
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        print(f"--- System Pulse [{timestamp}] ---")
        print(f"OS: {self.os_info} | CPU: {cpu_usage}% | RAM: {ram_usage}% | Disk: {disk_usage}%")

        # Alert Logic
        if cpu_usage > self.cpu_limit:
            print(f"ALERT: High CPU usage detected! ({cpu_usage}%)")
        
        if ram_usage > self.ram_limit:
            print(f"CRITICAL: RAM nearly full! ({ram_usage}%)")

    def run_monitor(self, duration_seconds=60):
        print(f"Starting monitor (Limits: CPU {self.cpu_limit}%, RAM {self.ram_limit}%)")
        try:
            while True:
                self.check_vitals()
                time.sleep(5) # Check every 5 seconds
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user.")

if __name__ == "__main__":
    monitor = SystemPulse(cpu_limit=70, ram_limit=80)
    monitor.run_monitor()