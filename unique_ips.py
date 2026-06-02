unique_ips = set()

with open("ip_list.txt", "r") as file:
    for line in file:
        ip = line.strip()
        unique_ips.add(ip)

print("unique IPs:")

for ip in unique_ips:
    print(ip)