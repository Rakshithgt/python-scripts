import re 

status_count = {}

status_pattern = r'"\s(\d{3})'

with open("access_log.txt", "r") as file:
    for line in file:
        match = re.search(status_pattern, line)

        if match:
            status_code = match.group(1)
            status_count[status_code] = status_count.get(status_code, 0) + 1

print ("HTTP Status code Report")

for status_code, count in status_count.items():
    print(status_code, "appeared", count, "times")