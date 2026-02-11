import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_charts():
    # Path to the data we created in Project 08
    data_path = "../Project8_NetAnalyzer/performance_summary.csv"

    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found! Run Project 08 first.")
        return

    # 1. Load the analyzed data
    df = pd.read_csv(data_path)

    # 2. Create the Figure (The Canvas)
    plt.figure(figsize=(10, 6))

    # 3. Build the Bar Chart
    # We use 'Website' for X and 'Avg Speed (ms)' for Y
    plt.bar(df['Website'], df['Avg Speed (ms)'], color=['#4285F4', '#34A853', '#EA4335'])

    # 4. Add Styling (The "Lead" touch)
    plt.title('Network Performance Comparison', fontsize=16)
    plt.xlabel('Website', fontsize=12)
    plt.ylabel('Average Latency (ms)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # 5. Save the Chart as an Image
    plt.savefig('network_report.png')
    print("✅ Success! 'network_report.png' has been generated.")
    
    # 6. Show the plot (This will open a window with your graph)
    plt.show()

if __name__ == "__main__":
    generate_charts()