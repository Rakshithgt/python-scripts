import re

error_count = {}

status_pattern = r'"\s(\d{3})'

with open ("access_log.txt", "r") as file:
    for line in file:
        match = re.search(status_pattern, line)
   
        if match:
            status_code = int(match.group(1))

        if status_code >= 400:
            error_count[status_code] = error_count.get(status_code, 0) + 1

print("HTTP Error Status Report")

for status_code, count in error_count.items():
    print(status_code, "appeared", count, "times")