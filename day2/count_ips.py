ip_count = {}

with open ("ip_list.txt", "r") as file:
    for line in file:
        ip = line.strip()
        ip_count[ip] = ip_count.get(ip, 0) + 1

print("IP Count Report:")

for ip, count in ip_count.items():
    print (ip, "appeared", count, "times")