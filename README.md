# SitePulse: A Simple Python Uptime Monitor 

Author: **Alex Teye Ametepey** *IT Student, University of Ghana*

## What is this?
I built this script to solve a simple problem: I wanted a way to check if my websites (or any sites I use frequently) are actually online without manually opening them every 10 minutes. 

It’s a lightweight monitor that "pings" a list of URLs and tells you if they are up, down, or just slow.

## Why it’s useful
- **Automatic Logging**: It creates a file called `uptime_log.csv` and saves the results there. This is great for seeing if a site has been unstable over a whole day.
- **Smart Checks**: It uses custom headers so that websites don't think it's a "bot" and block the request.
- **Error Handling**: If your internet is off or a site is completely dead, the script won't crash—it just logs the error and moves to the next one.

## How to get it running
1. Make sure you have the `requests` library installed:
   ```bash
   pip install requests

   The Data Output
The log file (uptime_log.csv) will look something like this:
timestamp,url,status_code,result
2026-02-06 00:10,https://google.com,200,ONLINE
2026-02-06 00:10,[suspicious link removed],200,ONLINE