import pandas as pd
import os

def run_analysis():
    # Points to the Project 07 folder we set up earlier
    data_path = "../Project7_NetWatcher_Monitor/network_stats.csv"

    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found! Run Project 07 first.")
        return

    # Load and process data with Pandas
    df = pd.read_csv(data_path)
    df['Latency (ms)'] = pd.to_numeric(df['Latency (ms)'], errors='coerce')

    print("\n--- Project 08: Network Performance Summary ---")
    
    # Calculate Mean, Min, and Max speed
    stats = df.groupby('Site')['Latency (ms)'].agg(['mean', 'min', 'max']).reset_index()
    stats.columns = ['Website', 'Avg Speed (ms)', 'Fastest', 'Slowest']
    
    print(stats.to_string(index=False))

    # Export for the team
    stats.to_csv("performance_summary.csv", index=False)
    print("\nAnalysis complete. Created 'performance_summary.csv'")

if __name__ == "__main__":
    run_analysis()