server_name = "devops-server"
env = "prod"
cpu_usage = 75
disk_usage = 50
disk_threshold = 80

print("Server Name: ", server_name)
print("Environment: ", env)
print("CPU Usage: ", cpu_usage)
print("Disk Usage: ", disk_usage)

if (disk_usage > disk_threshold):
    print("WARNING: Disk usage is high")
else:
    print("OK: Disk usage is normal")