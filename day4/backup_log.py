import os
import shutil
from datetime import datetime

log_file = "app.log.txt"
backup_folder = "backup.log"

if not os.path.exists(backup_folder):
    os.mkdir(backup_folder)

if os.path.exists(log_file):
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_file_name = f"app_{current_time}.log"
    backup_file_path = os.path.join(backup_folder, backup_file_name)

    shutil.copy(log_file, backup_file_path)

    print("log backup created:", backup_file_path)
else:
    print("log file not found:", log_file)