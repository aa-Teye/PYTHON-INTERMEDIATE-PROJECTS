# Project 14: Enterprise Core Logger Engine

## Overview
A modular, Object-Oriented logging system designed for high-reliability applications. This project demonstrates advanced Python concepts including class inheritance, encapsulation, and custom exception handling.

## System Architecture
The engine is split into a two-tier hierarchy to ensure code reusability:

1. **BaseLogger**: Handles the core logic for timestamping and message formatting.
2. **ProductionLogger**: Inherits from the BaseLogger and handles physical file I/O and console output.



## Technical Features
- **Thread-Safe Append**: Uses standard file 'append' mode to ensure logs aren't overwritten.
- **Custom Exceptions**: Implements a dedicated `LogError` class for better debugging of filesystem issues.
- **Namespace Management**: Uses a professional package structure with `__init__.py` for modular imports.

## How to Run
1. Navigate to the root directory.
2. Run the implementation: `python main.py`
3. View the persistent logs in `system.log`.