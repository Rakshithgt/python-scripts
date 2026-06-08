import os
import shutil
from datetime import datetime

log_files = ["app.log.txt", "log_analysis_report.txt", "access_log.txt"]
backup_folder = "backup_logs"

if not os.path.exists(backup_folder):
    os.mkdir(backup_folder)

current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

for log_file in log_files:
    if os.path.exists(log_file):
        backup_file_name = f"{log_file}_{current_time}.bak"
        backup_file_path = os.path.join(backup_folder, backup_file_name)

        shutil.copy (log_file, backup_file_path)

        print("backup created:", backup_file_path)
    else:
        print("log file not found:", log_file)

print("Backup process completed")