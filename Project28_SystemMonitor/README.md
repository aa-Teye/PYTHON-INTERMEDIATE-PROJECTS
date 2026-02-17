# Project 28: Sentinel System Monitor

## Overview
A performance analytics tool designed to monitor hardware utilization. It captures real-time telemetry data for CPU and RAM and generates a visual diagnostic report.

## Technical Features
- **Kernel Telemetry:** Leverages `psutil` for direct hardware polling.
- **Time-Series Analysis:** Maps resource consumption over a defined temporal window.
- **Diagnostic Export:** Renders performance trends into PNG format for system auditing.

## Usage
1. Run `python monitor.py`
2. Observe real-time logs in the console.
3. Review the generated `System_Report.png` for a visual summary.