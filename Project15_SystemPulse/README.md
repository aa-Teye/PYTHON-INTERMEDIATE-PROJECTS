# Project 15: System Pulse & Hardware Monitor

## Overview
A real-time hardware monitoring suite designed to track CPU, RAM, and Disk utilization. This tool implements threshold-based alerting to notify IT administrators when system resources exceed safe operating limits.

## Features
- **Real-Time Vitals**: Continuous monitoring of hardware resources.
- **Custom Thresholds**: Configure CPU and RAM alerts based on specific hardware capabilities.
- **Cross-Platform**: Compatible with Windows, macOS, and Linux via the `platform` module.



## How to Run
1. `pip install -r requirements.txt`
2. `python pulse.py`