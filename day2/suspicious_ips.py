ip_count = {}
threshold = 10

with open ("ip_list.txt", "r") as file:
    for line in file:
        ip = line.strip()

        if ip == "":
            continue

        ip_count[ip] = ip_count.get(ip, 0) + 1

print("suspicious IP Report")
print("----------------------")

for ip, count in ip_count.items():
    if count > threshold:
        print (ip, "appeared", count, "times")