import psutil
import os

def get_disk_stats(mountpoint):
    """Retrieves and formats disk usage data."""
    try:
        usage = psutil.disk_usage(mountpoint)
        return {
            "total": usage.total / (1024**3),
            "used": usage.used / (1024**3),
            "free": usage.free / (1024**3),
            "percent": usage.percent
        }
    except PermissionError:
        return None

def print_report(drive_name, stats):
    """Prints a clean status report for a specific drive."""
    status = "⚠️  LOW SPACE ALERT" if stats['percent'] > 90 else "✅ HEALTHY"
    print(f"\n--- Drive Report: {drive_name} ---")
    print(f"Total Capacity: {stats['total']:.2f} GB")
    print(f"Space Used:     {stats['used']:.2f} GB ({stats['percent']}%)")
    print(f"Space Free:     {stats['free']:.2f} GB")
    print(f"Status:         {status}")
    print("-" * 30)

def main():
    # 1. Gather available drives
    partitions = [p.mountpoint for p in psutil.disk_partitions()]
    
    print("========================================")
    print("   DISK GUARDIAN v2: INTERACTIVE CLI")
    print("========================================")
    print("Detected Storage Volumes:")
    
    for i, drive in enumerate(partitions, 1):
        print(f"[{i}] {drive}")
    
    run_all_index = len(partitions) + 1
    print(f"[{run_all_index}] Run Full System Audit (All Drives)")
    print("[0] Exit")

    # 2. User Interaction
    try:
        choice = int(input("\nSelect an option: "))

        if choice == 0:
            print("Exiting Guardian...")
            return

        # Handle 'Run All'
        if choice == run_all_index:
            print("\nExecuting full system audit...")
            for drive in partitions:
                stats = get_disk_stats(drive)
                if stats:
                    print_report(drive, stats)
        
        # Handle specific drive selection
        elif 1 <= choice <= len(partitions):
            selected_drive = partitions[choice - 1]
            stats = get_disk_stats(selected_drive)
            if stats:
                print_report(selected_drive, stats)
            else:
                print(f"\nError: Permission denied for {selected_drive}")
        else:
            print("\nInvalid selection. Please run the program again.")

    except ValueError:
        print("\nInput Error: Please enter a valid number.")

if __name__ == "__main__":
    main()