import pandas as pd

def distill_data(file_path):
    try:
        # 1. Load the data
        df = pd.read_csv(file_path)
        
        print("--- RAW DATA ---")
        print(df)
        
        # 2. Perform Analysis
        print("\n--- DATA DISTILLATION (STATISTICS) ---")
        avg_temp = df['Temp'].mean()
        max_rain = df['Rainfall'].max()
        
        
        print(f"Average Temperature: {avg_temp:.2f}°C")
        print(f"Highest Rainfall recorded: {max_rain}mm")
        
        # 3. Export a Summary Report
        summary = df.describe()
        summary.to_csv("data_summary.csv")
        print("\n[SUCCESS]: Summary report saved to 'data_summary.csv'")

    except FileNotFoundError:
        print("[ERROR]: The data.csv file was not found!")

if __name__ == "__main__":
    distill_data("data.csv")