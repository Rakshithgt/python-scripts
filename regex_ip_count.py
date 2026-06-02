
import re

ip_count = {}

pattern = r"\d+\.\d+\.\d+\.\d+"

with open ("ip_list.txt", "r") as file:
    for line in file:
        matches = re.findall(pattern, line)

        for ip in matches:
            ip_count[ip] = ip_count.get(ip, 0) + 1

print ("IP Count Report")
print ("------------")

for ip, count in ip_count.items():
    print(ip, "appeared", count, "times")

#--------------------#

import re

ip_count = {}

pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

with open("ip_list.txt", "r") as file:
    for line in file:
        matches = re.findall(pattern, line)

        for ip in matches:
            ip_count[ip] = ip_count.get(ip, 0) + 1

for ip, count in ip_count.items():
    print(ip, "appeared", count, "times")