import json, os, shutil
from datetime import datetime

BASE = "storage"
FS_FILE = f"{BASE}/fs.json"
BACKUP_DIR = f"{BASE}/backups"

def load_fs(default):
    os.makedirs(BASE, exist_ok=True)
    os.makedirs(BACKUP_DIR, exist_ok=True)
    if not os.path.exists(FS_FILE):
        with open(FS_FILE, "w") as f:
            json.dump(default, f, indent=4)
        print("FS dibuat.")
    with open(FS_FILE) as f:
        return json.load(f)

def save_fs(fs):
    with open(FS_FILE, "w") as f:
        json.dump(fs, f, indent=4)
    today = datetime.now().strftime("%Y%m%d")
    backup_file = f"{BACKUP_DIR}/fs_backup_{today}.json"
    if not os.path.exists(backup_file):
        shutil.copy(FS_FILE, backup_file)