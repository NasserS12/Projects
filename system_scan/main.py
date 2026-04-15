import shutil
import psutil
from datetime import datetime

def get_detailed_report():
    """Collect real-time system metrics from Ubuntu"""
    
    # 1. Capture the current time of the scan
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 2. Get Disk usage for the root directory
    disk = shutil.disk_usage("/")
    
    # 3. Get overall CPU load (1-second average)
    cpu_load = psutil.cpu_percent(interval=1)

    # 4. Get Memory usage (RAM and Swap)
    virtual_mem = psutil.virtual_memory()
    swap_mem = psutil.swap_memory()

    # 5. Identify the application using the most memory
    top_process = sorted(psutil.process_iter(['name', 'memory_percent']), 
                         key=lambda x: x.info['memory_percent'], 
                         reverse=True)[0]

    # 6. Capture Network I/O (Data sent and received)
    net_io = psutil.net_io_counters()

    # Consolidate all data into a clean dictionary
    report = {
        "timestamp": timestamp,
        "cpu_load": f"{cpu_load}%",
        "ram_usage": f"{virtual_mem.percent}%",
        "swap_usage": f"{swap_mem.percent}%",
        "disk_free_gb": f"{disk.free / (1024**3):.2f} GB",
        "top_app": top_process.info['name'],
        "net_sent": f"{net_io.bytes_sent / (1024**2):.2f} MB",
        "net_recv": f"{net_io.bytes_recv / (1024**2):.2f} MB"
    }
    
    return report

def display_detailed_report(data):
    """Format and print the system report to the console"""
    print(f"\n--- 🛡️  LIVE SYSTEM SCAN | {data['timestamp']} ---")
    print(f"📈 CPU Load:    {data['cpu_load']}")
    print(f"🧠 RAM Usage:   {data['ram_usage']} (Swap: {data['swap_usage']})")
    print(f"💾 Free Disk:   {data['disk_free_gb']}")
    print(f"🔝 Top Process: {data['top_app']}")
    print(f"🌐 Network:     Sent: {data['net_sent']} | Recv: {data['net_recv']}")
    print("-" * 50)

if __name__ == "__main__":
    # Get the latest system data
    results = get_detailed_report()
    
    # Show the results immediately
    display_detailed_report(results)