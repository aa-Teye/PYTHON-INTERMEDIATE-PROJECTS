

---

# Project 08: NetAnalyzer Statistics

## Overview

NetAnalyzer is a data analysis tool designed to process network performance logs. It reads raw data from `network_stats.csv` and uses the **Pandas** library to calculate key performance metrics, providing a clear summary of connection stability and speed.

## Features

* **Automated Data Loading**: Automatically locates and reads CSV logs from the Project 07 directory.
* **Statistical Calculation**: Computes Average (Mean), Minimum, and Maximum latency for each monitored website.
* **Data Export**: Generates a new `performance_summary.csv` for easy reporting.

## Installation

Ensure you have the required libraries installed:

```powershell
pip install -r requirements.txt

```

## Usage

Run the analysis script from the project directory:

```powershell
python analyzer.py

```

## File Structure

* `analyzer.py`: The main Python script containing the analysis logic.
* `requirements.txt`: List of necessary Python dependencies (Pandas).
* `performance_summary.csv`: The output file generated after running the script.

---

