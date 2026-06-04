from datetime import datetime

def server_health_status(server):
    cpu_threshold = 90
    disk_threshold = 90

    if server["cpu_usage"] > cpu_threshold or server["disk_usage"] > disk_threshold:
        return "UNHEALTHY"
    else: 
        return "HEALTHY"

servers = [
    {"name": "web01", "cpu_usage": 75, "disk_usage": 85},
    {"name": "app01", "cpu_usage": 60, "disk_usage": 70},
    {"name": "db01", "cpu_usage": 85, "disk_usage": 95},
]

current_time = datetime.now()

with open("server_health.txt", "w") as report_file:
    report_file.write(f"Server health Report\n")
    report_file.write(f"Generated at: {current_time}\n")
    report_file.write("------------------------------\n")

    for server in servers:
        status = server_health_status(server)
        line = f"{server['name']} - CPU: {server['cpu_usage']}%, - Disk: {server['disk_usage']}% - Status: {status}\n"

        report_file.write(line)
print("Server health created: server_health.txt")