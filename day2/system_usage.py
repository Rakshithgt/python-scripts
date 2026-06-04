import psutil

cpu_threshold = 80
disk_threshold = 90

cpu_usage = psutil.cpu_percent(interval=1)
disk_usage = psutil.disk_usage('C:/').percent


print("Current CPU Usage:", cpu_usage, "%")
print("Current Disk Usage:", disk_usage, "%")

if cpu_usage > cpu_threshold or disk_usage > disk_threshold:
    print("Status: UNHEALTHY")
else:
    print("Status: HEALTHY")