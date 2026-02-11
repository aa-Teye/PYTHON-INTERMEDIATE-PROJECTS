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
git 
