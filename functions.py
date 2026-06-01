def check_server_health(server):
    cpu_threshold = 75
    disk_threshold = 80

    print("----------------------------------------")
    print("Checking Server: ", server["name"])
    print("Cpu Usage: ", server["cpu_usage"])
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

servers = [
    {"name": "Server1", "cpu_usage": 65, "disk_usage": 70},
    {"name": "Server2", "cpu_usage": 80, "disk_usage": 85},
    {"name": "Server3", "cpu_usage": 50, "disk_usage": 60},
]

for server in servers:
    check_server_health(server)


#------------------------------------------------------

def check_server_health(server):
    cpu_threshold = 75
    disk_threshold = 85

    if server["cpu_usage"] > cpu_threshold or server["disk_usage"] > disk_threshold:
        return "UNHEALTHY"
    else:
        return "HEALTHY"
    
    servers = [
        {"name": "web01", "cpu_usage": 65, "disk_usage": 70},
        {"name": "db01", "cpu_usage": 80, "disk_usage": 60},
        {"name": "cache01", "cpu_usage": 50, "disk_usage": 90},
    ]
    
    for server in servers:
        status = check_server_health(server)

        print("----------------------------------------")
        print("Server: ", server["name"])
        print("Status:", status)

    