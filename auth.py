import json, os, getpass, hashlib
from colorama import Fore, Style

USER_FILE = "storage/users.json"

def hash_password(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def load_users(default):
    os.makedirs(os.path.dirname(USER_FILE), exist_ok=True)
    if not os.path.exists(USER_FILE):
        hashed_defaults = {}
        for u, data in default.items():
            data_copy = data.copy()
            data_copy["password"] = hash_password(data["password"])
            hashed_defaults[u] = data_copy
        with open(USER_FILE, "w") as f:
            json.dump(hashed_defaults, f, indent=4)
    with open(USER_FILE) as f:
        return json.load(f)

# Login sederhana, tapi sekarang gak dipake banyak (SUDO handle switch)
def login(users):
    u = input(Fore.CYAN + "Pengguna: " + Style.RESET_ALL)
    p = getpass.getpass("Kata sandi: ")
    hashed_p = hash_password(p)
    if u in users and users[u]["password"] == hashed_p:
        print(Fore.GREEN + "BERHASIL: Login berhasil." + Style.RESET_ALL)
        return u, users[u]["role"]
    print(Fore.RED + "KESALAHAN: Pengguna/kata sandi salah." + Style.RESET_ALL)
    return None, None