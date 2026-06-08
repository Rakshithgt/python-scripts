import re
from datetime import datetime

ip_count = {}
status_count = {}
error_count = {}

suspicious_threshold = 3


ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
status_pattern = r'"\s(\d{3})'


with open ("access_log.txt", "r") as file:
    for line in file:
        match = re.findall(ip_pattern, line)

        for ip in match:
            ip_count[ip] = ip_count.get(ip, 0) + 1

        matches = re.search(status_pattern, line)

        if matches:
            status_code = int(matches.group(1))

            status_count[status_code] = status_count.get(status_code, 0) + 1

            if status_code >= 400:
                error_count[status_code] = error_count.get(status_code, 0) + 1

total_requests = sum(status_count.values())
total_errors = sum(error_count.values())

if total_requests > 0:
    error_percentage = (total_errors / total_requests) * 100
else:
    error_percentage = 0

current_time = datetime.now()

with open ("log_analysis_practice.txt", "w") as report:
    report.write("Log Analysis Report \n")
    report.write(f"Generated At: {current_time}\n")
    report.write("----------------------------\n\n")

    report.write(f"Total requests :{total_requests}\n")
    report.write(f"Total Errors: {total_errors}\n")
    report.write(f"Unique IPs: {len(ip_count)}\n")
    report.write(f"Error Percentage: {error_percentage:.2f}%\n\n")

    report.write ("IP Request Count\n")
    report.write ("---------------------")
    for ip, count in sorted(ip_count.items(), key=lambda item: item[1], reverse=True):
        report.write(f"{ip} made {count} requests \n")

    report.write ("\nSusupicious IPs\n")
    report.write ("---------------------\n")
    for ip, count in sorted(ip_count.items(), key=lambda item: item[1], reverse=True):
        if count > suspicious_threshold:
            report.write(f"{ip} is suspicious with {count} requests \n")

    report.write("\nHTTP Status Code Count\n")
    report.write ("---------------------\n")
    for status_code, count in sorted(status_count.items(), key=lambda item: item[1], reverse=True):
            report.write(f"{status_code} appeared {count} times \n")


    report.write("\nHTTP Error Status Count\n")
    report.write ("---------------------\n")
    for status_code, count in sorted(error_count.items(), key=lambda item: item[1], reverse=True):
            report.write(f"{status_code} appeared {count} times \n")


print("log analysis report created: log_analysis_report_practice.txt")