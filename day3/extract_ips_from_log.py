import re

pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

with open ("access_log.txt", "r") as file:
    for line in file:
        matches = re.findall(pattern, line)

        for ip in matches:
            print(ip)