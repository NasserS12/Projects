import shutil
import psutil
from datetime import datetime
import time
import os
import sys
import json

def get_detailed_report():
    """
    Collects system metrics including CPU, RAM, Disk, Network, 
    and identifies the top 3 resource-consuming processes.
    """
    
    # Get current date and time for the report
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Get disk usage statistics for the root directory
    disk = shutil.disk_usage("/")
    
    # Capture system-wide resource metrics
    # interval=1 means it monitors CPU usage over 1 second for better accuracy
    cpu_load = psutil.cpu_percent(interval=1)
    virtual_mem = psutil.virtual_memory()
    swap_mem = psutil.swap_memory()
    net_io = psutil.net_io_counters()
    
    # TOP 3 PROCESSES LOGIC:
    # We iterate through all running processes and fetch their PID, Name, CPU, and RAM usage.
    # We sort them based on a combined score (CPU % + RAM %).
    top_processes = sorted(
        psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']),
        key=lambda x: (x.info['cpu_percent'] or 0) + (x.info['memory_percent'] or 0),
        reverse=True
    )[:3]
    
    # Format the top 3 processes into a clean list of dictionaries
    top_apps = []
    for i, p in enumerate(top_processes, 1):
        cpu_val = p.info['cpu_percent'] or 0
        ram_val = p.info['memory_percent'] or 0
        top_apps.append({
            'rank': i,
            'name': p.info['name'],
            'pid': p.info['pid'],
            'cpu': f"{cpu_val:.1f}%",
            'ram': f"{ram_val:.1f}%",
            'score': f"{(cpu_val + ram_val):.1f}%"
        })
    
    # Construct the final report dictionary
    report = {
        "timestamp": timestamp,
        "cpu_load": f"{cpu_load:.1f}%",
        "ram_usage": f"{virtual_mem.percent:.1f}%",
        "swap_usage": f"{swap_mem.percent:.1f}%",
        "disk_free_gb": f"{disk.free / (1024**3):.2f}",
        "disk_total_gb": f"{disk.total / (1024**3):.2f}",
        "net_sent_mb": f"{net_io.bytes_sent / (1024**2):.2f}",
        "net_recv_mb": f"{net_io.bytes_recv / (1024**2):.2f}",
        "top_apps": top_apps,
        "total_processes": len(psutil.pids()) # Optimized: gets count of process IDs
    }
    
    return report

def display_report(data):
    """Prints the formatted report to the terminal with a clean UI"""
    print(f"\n{'='*80}")
    print(f"SYSTEM STATUS REPORT | {data['timestamp']} {'='*25}")
    print(f"CPU Load:         {data['cpu_load']}")
    print(f"RAM Usage:        {data['ram_usage']} (Swap: {data['swap_usage']})")
    print(f"Disk Space:       Free: {data['disk_free_gb']}GB / Total: {data['disk_total_gb']}GB")
    print(f"Network I/O:      Sent: {data['net_sent_mb']}MB | Received: {data['net_recv_mb']}MB")
    print(f"Total Processes:  {data['total_processes']:,}")
    
    print(f"\nTOP 3 PROCESSES (CPU+RAM Score):")
    print("-" * 60)
    for app in data['top_apps']:
        print(f"  {app['rank']} {app['name']:25s} | CPU: {app['cpu']:>6s} | RAM: {app['ram']:>6s} | Score: {app['score']}")
    
    print(f"{'='*80}\n")

def save_report(data, filename=None):
    """Exports the collected data into a JSON file for history tracking"""
    if not filename:
        # Create a unique filename based on the current timestamp
        filename = f"system-report-{data['timestamp'].replace(' ', '_').replace(':', '-')}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Report saved: {filename}")

def continuous_monitoring(interval=5, max_reports=100):
    """Runs the scanner repeatedly at set intervals until stopped or limit reached"""
    reports_count = 0
    print(f"Starting continuous monitoring (every {interval}s) - Ctrl+C to stop")
    
    try:
        while True:
            data = get_detailed_report()
            display_report(data)
            
            # Logic: Automatically save data to a file every 10 scan cycles
            if reports_count % 10 == 0:
                save_report(data)
            
            reports_count += 1
            if reports_count >= max_reports:
                print(f"Reached limit of {max_reports} reports.")
                break
            
            print(f"Next scan in {interval}s... ", end='', flush=True)
            time.sleep(interval)
            print()
            
    except KeyboardInterrupt:
        # Graceful shutdown when user presses Ctrl+C
        print("\nMonitoring stopped by user")
        save_report(data, "final-report.json")

if __name__ == "__main__":
    # Command line argument handling logic
    if len(sys.argv) > 1:
        # Case: python monitor.py continuous [interval]
        if sys.argv[1] == "continuous":
            interval = int(sys.argv[2]) if len(sys.argv) > 2 else 5
            continuous_monitoring(interval)
        # Case: python monitor.py save
        elif sys.argv[1] == "save":
            data = get_detailed_report()
            display_report(data)
            save_report(data)
    else:
        # Default Case: Run a single scan and show help instructions
        data = get_detailed_report()
        display_report(data)
        save_report(data)
        print("Usage:")
        print("  python monitor.py              # Single scan")
        print("  python monitor.py save         # Single scan + save")
        print("  python monitor.py continuous   # Continuous monitoring")
        print("  python monitor.py continuous 10 # Every 10 seconds")