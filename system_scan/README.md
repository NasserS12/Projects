# 🛡️ Ubuntu System Monitor

A lightweight Python utility to display real-time system health metrics on Ubuntu.

##  Features
* **Live CPU Tracking**: Monitor overall processor load.
* **Memory Analysis**: Tracks both Physical RAM and Swap usage.
* **Storage Watch**: View free disk space in GB.
* **Top Process**: Automatically finds the most memory-intensive app.
* **Network Traffic**: Displays network data sent and received in MB.

##  Requirements
* Python 3.x
* `psutil`(External Library)
* `shutil` (Built-in)
* `datetime` (Built-in)

To install the required external library, run:
```bash
pip3 install psutil
