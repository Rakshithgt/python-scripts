def check_server_health(server):
    cpu_threshold = 75
    disk_threshold = 80

    if server["cpu_usage"] > cpu_threshold or server["disk_usage"] > disk_threshold:
        return "UNHEALTHY"
    else:
        return "HEALTHY"

def send_alert(server_name):
    print("ALERT: Sending alert for server:", server_name)

servers = [
    {"name": "web01", "cpu_usage": 45, "disk_usage": 50},
    {"name": "app01", "cpu_usage": 82, "disk_usage": 60},
    {"name": "db01", "cpu_usage": 55, "disk_usage": 91}
]

for server in servers:
    status = check_server_health(server)

    print("--------------------")
    print("Server:", server["name"])
    print("Status:", status)

    if status == "UNHEALTHY":
        send_alert(server["name"])