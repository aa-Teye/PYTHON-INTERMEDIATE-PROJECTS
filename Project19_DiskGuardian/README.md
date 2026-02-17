# Project 19: Disk Space Guardian

## Overview
The Disk Space Guardian is a system utility developed to monitor storage health. It is designed to provide automated oversight of disk utilization, specifically for environments where large media files or software builds are frequent. This tool assists in preventing data loss and system instability by alerting the user before storage reaches critical capacity.

## Technical Features
- Disk Analysis: Retrieves total, used, and free space directly from the operating system.
- Data Conversion: Scales raw byte data into Gigabytes (GB) using binary prefix calculations.
- Threshold Alerts: Automatically identifies and flags volumes exceeding 90% utilization.
- Volume Compatibility: Configurable to target any mapped drive or mount point (e.g., C:/ or F:/).

## Technical Specifications
- Language: Python 3.10+
- Dependencies: psutil 5.9.8
- Core Concepts: System I/O, Data Scaling, and Exception Handling for missing hardware.

## Installation and Execution
1. Navigate to the project directory: Project19_DiskGuardian.
2. Install the required system utility library:
   pip install psutil
3. Execute the script:
   python guardian.py

## Portfolio Context
This project demonstrates competency in system resource management and DevOps automation. It bridges the gap between high-level Python programming and low-level system administration.