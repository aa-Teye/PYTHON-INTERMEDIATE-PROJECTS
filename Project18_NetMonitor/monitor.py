import os
import platform
import time
import subprocess

def check_server(hostname):
    # Determine the correct flag: Windows uses '-n', others use '-c'
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    # Build the command: ping -n 1 hostname
    command = ['ping', param, '1', hostname]
    
    # Run the command and capture the result
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Return True if the server responded (returncode 0)
    return result.returncode == 0

def run_monitor():
    # Targets: Church site, Google (DNS), and Github
    targets = ["google.com", "8.8.8.8", "github.com", "st.ug.edu.gh"]
    
    print(f"\n--- [NETWORK AUDIT: {time.ctime()}] ---")
    
    for target in targets:
        if check_server(target):
            print(f"✅ {target.ljust(15)} | Status: ONLINE")
        else:
            print(f"❌ {target.ljust(15)} | Status: OFFLINE (Alert!)")

if __name__ == "__main__":
    try:
        while True:
            run_monitor()
            print("\nChecking again in 60 seconds... (Ctrl+C to stop)")
            time.sleep(60)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")