import psutil
import shutil
import os

def check_disk_usage(drive_path):
    # Get disk usage statistics
    usage = psutil.disk_usage(drive_path)
    
    # Convert bytes to Gigabytes for readability
    total_gb = usage.total / (1024**3)
    used_gb = usage.used / (1024**3)
    free_gb = usage.free / (1024**3)
    percent = usage.percent

    print(f"\n--- [Disk Health Report: {drive_path}] ---")
    print(f"Total: {total_gb:.2f} GB")
    print(f"Used:  {used_gb:.2f} GB ({percent}%)")
    print(f"Free:  {free_gb:.2f} GB")

    # The "Guardian" Logic: Alert if free space is less than 10%
    if percent > 90:
        print("\n ALERT: Disk space is critically low! Time to clean up.")
    else:
        print("\ Disk space is within healthy limits.")

if __name__ == "__main__":
    # You can change this to 'C:/' or any drive you want to monitor
    target_drive = 'F:/' 
    
    if os.path.exists(target_drive):
        check_disk_usage(target_drive)
    else:
        print(f"Drive {target_drive} not found. Checking C:/ instead.")
        check_disk_usage('C:/')