import re

text = "ERROR: Disk usage is 95% on server db01"

pattern = r"\d+%"

match = re.search(pattern, text)

if match:
    print("Found:", match.group())
else:
    print("No percentage found")


#--------------------#

import re

text = "CPU 85%, Disk 91%, Memory 70%"

pattern = r"\d+%"

matches = re.findall(pattern, text)

print(matches)

#-------------------------#

import re

line = "2026-06-02 10:30:45 ERROR Disk space is full"

pattern = r"ERROR"

if re.search(pattern, line):
    print("ERROR found")


#-------------------------#

import re

line = "2026-06-02 10:30:45 Warning CPU usage is high"

pattern = r"ERROR|Warning"

if re.search(pattern, line):
    print("Pattern is present")


#-------------------------#

import re

text = "Server IP is 192.168.1.25"

pattern = r"\d+\.\d+\.\d+\.\d+"

match = re.search(pattern, text)

if match:
  print("IP address:", match.group())


#-------------------------#

import re

text = "Alert received from the server web-prod-01"

pattern = r"server ([\w-]+)"

match = re.search(pattern, text)

if match:
    print("Server name:", match.group(1))


#-------------------------#

import re

text = "CPU usage is 87%"

pattern = r"CPU usage is (\d+)%"

match = re.search(pattern, text)
if match:
    cpu_usage =  match.group(1)
    print("CPU Usage:", cpu_usage)

#-------------------------#

import re

text = "Backup completed on 2026-06-02"

pattern = r"\d{4}-\d{2}-\d{2}"

match = re.search(pattern, text)

if match:
    print("Date:", match.group())


#-------------------------#

import re

text = "Job started at 14:35:20"

pattern = r"\d{2}:\d{2}:\d{2}"

match = re.search(pattern, text)

if match:
    print("Time:", match.group())


#-------------------------#


import re

email = "admin@example.com"

pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

if re.search(pattern, email):
    print("Valid email")
else:
    print("Invalid email")


#-------------------------#

import re

filename = "application.log"

pattern = r"\.log$"

if re.search(pattern, filename):
    print("this is a log file")


#-------------------------#

import re

line = 'GET /api/users 500 120ms'

pattern = r"\s(\d{3})\s"

match = re.search(pattern, line)

if match:
    print("Status Code:", match.group(1))



#-------------------------#

\d      digit, 0-9
\w      word character: letters, numbers, underscore
\s      whitespace
.       any character
+       one or more
*       zero or more
?       optional
{3}     exactly 3 times
{2,4}   between 2 and 4 times
^       start of line
$       end of line
|       OR
()      capture group
[]      character set