servers = [
    {"name": "web01", "cpu_usage": 90, "disk_usage": 50},
    {"name": "app01", "cpu_usage": 60, "disk_usage": 70},
    {"name": "db01", "cpu_usage": 70, "disk_usage": 75},
]

cpu_threshold = 80
disk_threshold = 80

for server in servers:
    print("-------------")
    print("Checking Server: ", server["name"])
    print("CPU Usage: ", server["cpu_usage"])
    print("Disk Usage: ", server["disk_usage"])

    is_healthy = True

    if server["cpu_usage"] > cpu_threshold:
        print("Issue: CPU usage is high")
        is_healthy = False

    if server["disk_usage"] > disk_threshold:
        print("Issue: Disk usage is high")
        is_healthy = False

    if is_healthy:
        print("overall status: Healthy")
    else:
        print("overall status: Unhealthy")