# System Resource Monitor

A lightweight Python-based utility to monitor system performance in real-time. This tool tracks CPU load, RAM usage, disk space, network I/O, and identifies the top 3 resource-consuming processes.

## Features
- **Real-time Monitoring:** Get instant snapshots of your system health.
- **Top Processes Analysis:** Automatically calculates a 'Score' (CPU + RAM) to identify heavy applications.
- **Continuous Mode:** Run the scanner at custom intervals (e.g., every 5 seconds).
- **Data Persistence:** Automatically saves reports to JSON format for later analysis.
- **No-Emoji/Professional UI:** Clean terminal output suitable for server environments.

## Prerequisites
This script requires the `psutil` library. You can install it via pip3:
```bash
pip3 install psutil
