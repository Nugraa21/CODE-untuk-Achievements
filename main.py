from filesystem import load_fs, save_fs
from auth import load_users
from shell import shell
import json, os

DEFAULT_FS = {
    "/": {
        "home": {
            "nugra": {
                "readme.txt": "Selamat datang di Nugra21.SaWiT-OS 🌴"
            }
        }
    }
}

DEFAULT_USERS = {
    "nugra": {"password": "rakyat123", "role": "rakyat"},
    "pejabat": {"password": "admin123", "role": "pejabat"}
}

SYSTEM_FILE = "storage/system.json"
if not os.path.exists(SYSTEM_FILE):
    with open(SYSTEM_FILE, "w") as f:
        json.dump({
            "os": "Nugra21.SaWiT-OS",
            "version": "1.0 MODULAR",
            "kernel": "SawitKernel",
            "creator": "Ludang Prasetyo Nugroho"
        }, f, indent=4)

with open(SYSTEM_FILE) as f:
    system = json.load(f)

fs = load_fs(DEFAULT_FS)
users = load_users(DEFAULT_USERS)

shell(fs, users, system, save_fs)
