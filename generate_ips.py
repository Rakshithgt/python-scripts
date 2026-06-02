import random

base_ips = [
    "192.168.1.10",
    "192.168.1.11",
    "192.168.1.12",
    "10.0.0.5",
    "10.0.0.6",
    "172.16.0.20",
    "172.16.0.21",
]

ips = []

with open("ip_list.txt", "w") as file:
    for  i in range(100):
        ip = random.choice(base_ips)
        file.write(ip + "\n")

print("100 IPS created in the ip_list.txt")