# Project 22: Password Sentinel

## Overview
Password Sentinel is a cybersecurity utility designed to audit the cryptographic strength of user-defined passwords. It evaluates security through a multi-layered approach, combining pattern recognition (Regex) with a prohibited-word blacklist to ensure passwords are both complex and unpredictable.

## Technical Features
- **Entropy Analysis:** Evaluates passwords based on length, casing, numerical inclusion, and special character density.
- **Prohibited Word Detection:** Implements a blacklist to flag common or easily guessable terms (e.g., 'admin', 'password', 'ghana'), preventing dictionary-based attacks.
- **Interactive CLI:** Built with a continuous loop for real-time, iterative testing.
- **Regex Integration:** Utilizes Python's `re` module for high-precision string pattern matching.

## Technical Specifications
- **Language:** Python 3.10+
- **Modules:** `re` (Regular Expressions)
- **Concepts:** Data Validation, Weighted Scoring Algorithms, Logic Branching.

## Installation and Execution
1. Navigate to the project directory: `Project22_PasswordSentinel`.
2. Run the application:
   ```bash
   python sentinel.py