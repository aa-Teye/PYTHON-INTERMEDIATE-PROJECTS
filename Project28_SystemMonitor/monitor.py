import psutil
import matplotlib.pyplot as plt
import time

def monitor_system(duration=10):
    cpu_usage = []
    ram_usage = []
    timestamps = []

    print(f"--- Monitoring System for {duration} seconds ---")
    
    for i in range(duration):
        # 1. Capture Hardware Data
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        
        cpu_usage.append(cpu)
        ram_usage.append(ram)
        timestamps.append(i)
        
        print(f"Sec {i+1}: CPU: {cpu}% | RAM: {ram}%")

    # 2. Generate Visual Report
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, cpu_usage, label='CPU Usage (%)', color='red', marker='o')
    plt.plot(timestamps, ram_usage, label='RAM Usage (%)', color='blue', marker='s')
    
    plt.title("Sentinel System Performance Report", fontsize=14)
    plt.xlabel("Time (Seconds)")
    plt.ylabel("Usage Percentage")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # 3. Save the Analytics
    report_name = "System_Report.png"
    plt.savefig(report_name)
    print(f"\n✅ Report generated: {report_name}")
    plt.show()

if __name__ == "__main__":
    # Increase duration for a longer "solid" test
    monitor_system(duration=15)