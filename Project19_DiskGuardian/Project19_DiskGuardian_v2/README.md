# Project 19: Disk Space Guardian (Version 2)

## Overview
An interactive Command Line Interface (CLI) tool designed for comprehensive system storage monitoring. This version introduces dynamic drive detection and user-selected audit paths.

## Features
- Dynamic Volume Discovery: Automatically detects all mounted drives and partitions.
- User-Selected Audits: Numbered menu system for specific drive targeting.
- Batch Processing: "Run All" feature for full system health snapshots.
- Unit Conversion: Transforms raw data into Gigabytes (GB) for high readability.

## Installation
1. Navigate to Project19_DiskGuardian_v2.
2. Install dependencies:
   pip install psutil
3. Execute:
   python guardian_v2.py