server_name = "web-server-01"
Environment = "production"

cpu_usage = 50
disk_usage = 90

cpu_threshold = 75
disk_threshold = 80

print("Server Name: ", server_name)
print("Environment: ", Environment)
print("CPU Usage: ", cpu_usage)
print("Disk Usage: ", disk_usage)

is_healthy = True

if cpu_usage > cpu_threshold:
    print("Issue: CPU usage is high")
    is_healthy = False

if disk_usage > disk_threshold:
    print("Issue: Disk usage is high")
    is_healthy = False
    
if is_healthy:
    print("server is healthy")
else:
    print("server is not healthy")
