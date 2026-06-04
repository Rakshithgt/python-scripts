def check_server_health(server):
    cpu_threshold = 80
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

with open("server_health_report.txt", "w") as report_file:
    for server in servers:
        status = check_server_health(server)

        line = f"{server['name']} - CPU: {server['cpu_usage']}% - Disk {server['disk_usage']}% - Status: {status}\n"
    
        report_file.write(line)

print("Health report created: server_health_report.txt")
    

