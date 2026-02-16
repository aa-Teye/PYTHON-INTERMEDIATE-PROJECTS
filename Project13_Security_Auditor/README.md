Project 13: Web Performance and Security Header Auditor
Overview
This tool is designed to benchmark server response times and audit critical security headers. In a production environment, simply having a "working" website isn't enough; the server must be fast and configured to defend against common web-based vulnerabilities. This script automates that verification process.

Key Audit Metrics
The auditor evaluates two primary categories:

1. Performance (Latency)
The script calculates the Time to First Byte (TTFB) by measuring the round-trip time between the request and the server's response. This helps identify slow server configurations or network bottlenecks.

2. Security Headers
It scans the server's response for the following industry-standard security headers:

Strict-Transport-Security (HSTS): Ensures all communication is sent over HTTPS.

Content-Security-Policy (CSP): Protects against Cross-Site Scripting (XSS).

X-Frame-Options: Prevents clickjacking attacks.

X-Content-Type-Options: Prevents the browser from "sniffing" the content type.

How it Works
Initiates a standard HTTP GET request using professional browser-emulation headers.

Captures the high-resolution timestamp to determine latency in milliseconds.

Parses the Response Header Dictionary to verify the presence of security flags.

Generates a JSON Report (audit_report.json) for technical review.

Setup and Execution
Install dependencies:

Bash
pip install -r requirements.txt
Run the auditor:

Bash
python auditor.py