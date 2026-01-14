from filesystem import load_fs, save_fs
from auth import load_users
from shell import shell
from ui import loading_message
from colorama import Fore, Style
import json, os

CONFIG = {
    "theme": "sawit_green",
    "auto_save_interval": 5
}

DEFAULT_FS = {
    "/": {
        "home": {
            "nugra": {
                "readme.txt": "Selamat datang di Nugra21.SaWiT-OS.\nTanam kode, panen keterampilan.",
                "projects": {
                    "sawit.py": "# Contoh skrip sawit\nprint('Halo Sawit!')"
                }
            },
            "shared": {
                "motivasi.txt": "Sawit: Hijau, Kuat, Masa Depan."
            }
        },
        "bin": {
            "help.txt": "Bantuan SaWiT OS"
        }
    }
}

# Fix: User "nugra" default role "rakyat", "pejabat" untuk admin, pw sama "123"
DEFAULT_USERS = {
    "nugra": {"password": "123", "role": "rakyat"},
    "pejabat": {"password": "123", "role": "pejabat"}
}

SYSTEM_FILE = "storage/system.json"
if not os.path.exists(SYSTEM_FILE):
    with open(SYSTEM_FILE, "w") as f:
        json.dump({
            "os": "Nugra21.SaWiT-OS",
            "version": "1.1 SAWIT-ENHANCED",
            "kernel": "SawitKernel v2.0",
            "creator": "Ludang Prasetyo Nugroho",
            "uptime": "Boot baru"
        }, f, indent=4)

with open(SYSTEM_FILE) as f:
    system = json.load(f)

print(Fore.CYAN + "Memulai SaWiT OS..." + Style.RESET_ALL)
loading_message("Inisialisasi filesystem")
loading_message("Muat pengguna & autentikasi")
loading_message("Luncurkan shell")

fs = load_fs(DEFAULT_FS)
users = load_users(DEFAULT_USERS)

shell(fs, users, system, save_fs)