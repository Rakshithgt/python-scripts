import re
from datetime import datetime

ip_count = {}
error_count = {}
status_count = {}

suspicious_threshold = 2

ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
status_pattern = r'"\s(\d{3})'

with open ("access_log.txt", "r") as file:
    for line in file:
        ips = re.findall(ip_pattern, line)

        for ip in ips:
            ip_count[ip] = ip_count.get(ip, 0) + 1

        status_match = re.search(status_pattern, line)

        if status_match:
            status_code = int(status_match.group(1))

            status_count[status_code] = status_count.get(status_code, 0) + 1

            if status_code >= 400:
                error_count[status_code] = error_count.get(status_code, 0) + 1

current_time = datetime.now()

with open ("log_analysis_report.txt", "w") as report:
    report.write("log analysis Report\n")
    report.write(f"Generated at: {current_time}\n")
    report.write("---------------\n\n")

    report.write("IP Request Count\n")
    report.write("-----------\n")
    for ip, count in ip_count.items():
        report.write(f"{ip} made {count} requests\n")

    report.write("Suspicious IPs\n")
    report.write("-----------\n")
    for ip, count in ip_count.items():
        if count > suspicious_threshold:
            report.write(f"{ip} is suspicious with {count} times\n")

    report.write("HTTP Status Code Count\n")
    report.write("-----------\n")
    for status_code, count in status_count.items():
        report.write(f"{status_code} appeared {count} times\n")

    report.write("HTTP Error Status  Count\n")
    report.write("-----------\n")
    for status_code, count in status_count.items():
        report.write(f"{status_code} appeared {count} times\n")

print ("Log analysis report created: log_analysis_report.txt")