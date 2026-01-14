import os, json, datetime, getpass
from colorama import Fore, Style, init
init(autoreset=True)

# ===============================
# PATH
# ===============================
BASE = "storage"
FS_FILE = f"{BASE}/fs.json"
USER_FILE = f"{BASE}/users.json"
SYS_FILE = f"{BASE}/system.json"
os.makedirs(BASE, exist_ok=True)

# ===============================
# LOAD & SAVE
# ===============================
def load(path, default):
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(default, f, indent=4)
    with open(path) as f:
        return json.load(f)

def save(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

# ===============================
# DEFAULT DATA
# ===============================
fs = load(FS_FILE, {
    "/": {
        "home": {
            "nugra": {
                "readme.txt": "Selamat datang di Nugra21.SaWiTOS 🌴",
                "todo.txt": "1. Ngoding\n2. Push GitHub\n3. Jadi Pejabat"
            }
        }
    }
})

users = load(USER_FILE, {
    "nugra": {"password": "123", "role": "user"},
    "pejabat": {"password": "admin", "role": "pejabat"}
})

system = load(SYS_FILE, {
    "os": "Nugra21.SaWiTOS",
    "version": "2.0 MONOCHROME",
    "kernel": "SawitKernel 0.2",
    "creator": "Ludang Prasetyo Nugroho",
    "boot": str(datetime.datetime.now())
})

# ===============================
# SESSION
# ===============================
user = "nugra"
role = users[user]["role"]
cwd = ["/", "home", "nugra"]
history = []

# ===============================
# FILESYSTEM
# ===============================
def curdir():
    d = fs
    for p in cwd:
        d = d[p]
    return d

def pwd():
    return "/" if cwd == ["/"] else "/".join(cwd)

# ===============================
# UI
# ===============================
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    clear()
    print(Fore.WHITE + "┌──────────────────────────────────────────┐")
    print(Fore.WHITE + "│" + Fore.GREEN + "        NUGRA21.SaWiTOS TERMINAL        " + Fore.WHITE + "│")
    print(Fore.WHITE + "│" + Fore.CYAN + "   Fake Linux OS - Python Based 🌴      " + Fore.WHITE + "│")
    print(Fore.WHITE + "└──────────────────────────────────────────┘")
    print(Fore.YELLOW + "Ketik BANTUAN untuk melihat command\n")

def prompt():
    tag = Fore.RED + "#PEJABAT" if role == "pejabat" else Fore.GREEN + "$"
    return f"{Fore.CYAN}{user}@sawitos{Fore.WHITE}:{Fore.YELLOW}{pwd()} {tag} {Style.RESET_ALL}"

# ===============================
# TREE
# ===============================
def tree(d, pad=""):
    for k, v in d.items():
        print(pad + Fore.WHITE + "├── " + Fore.CYAN + k)
        if isinstance(v, dict):
            tree(v, pad + "│   ")

# ===============================
# COMMANDS
# ===============================
COMMANDS = {
    "LIHAT": "List direktori",
    "MASUK": "Masuk direktori",
    "MUNDUR": "Kembali",
    "POSISI": "Path aktif",
    "BUKA": "Buat folder",
    "BAKAR": "Hapus folder (PEJABAT)",
    "KEBUN": "Tree direktori",
    "TANAM": "Buat file",
    "PANEN": "Baca file",
    "RAWAT": "Edit file",
    "TEBANG": "Hapus file",
    "CANGKOK": "Copy file",
    "PINDAH": "Pindah file",
    "GANTI": "Rename file",
    "BERSIHKAN": "Clear layar",
    "CLS": "Alias clear",
    "WAKTU": "Waktu sistem",
    "SIAPA": "User aktif",
    "INFO_SAWIT": "Info OS",
    "NEOFETCH": "Info sistem ala Linux",
    "RIWAYAT": "History command",
    "SU": "Ganti user",
    "SUDO": "Mode pejabat",
    "BANTUAN": "List command",
    "SAWIT": "Easter egg 🌴",
    "EXIT": "Keluar OS",
    "PULANG": "Keluar OS"
}

# ===============================
# SHELL
# ===============================
def shell():
    global user, role
    banner()

    while True:
        cmd = input(prompt()).strip()
        history.append(cmd)
        if not cmd:
            continue
        a = cmd.split()
        c = a[0].upper()

        try:
            if c == "LIHAT":
                print("  ".join(curdir().keys()))

            elif c == "MASUK":
                if a[1] in curdir():
                    cwd.append(a[1])

            elif c == "MUNDUR":
                if len(cwd) > 1:
                    cwd.pop()

            elif c == "POSISI":
                print(pwd())

            elif c == "BUKA":
                curdir()[a[1]] = {}

            elif c == "BAKAR":
                if role == "pejabat":
                    del curdir()[a[1]]
                else:
                    print(Fore.RED + "Akses ditolak")

            elif c == "KEBUN":
                tree(curdir())

            elif c == "TANAM":
                curdir()[a[1]] = ""

            elif c == "PANEN":
                print(curdir()[a[1]])

            elif c == "RAWAT":
                print("Edit mode (:simpan)")
                isi = []
                while True:
                    l = input()
                    if l == ":simpan":
                        break
                    isi.append(l)
                curdir()[a[1]] = "\n".join(isi)

            elif c == "TEBANG":
                del curdir()[a[1]]

            elif c == "CANGKOK":
                curdir()[a[2]] = curdir()[a[1]]

            elif c == "PINDAH":
                curdir()[a[2]] = curdir().pop(a[1])

            elif c == "GANTI":
                curdir()[a[2]] = curdir().pop(a[1])

            elif c in ["BERSIHKAN", "CLS"]:
                banner()

            elif c == "WAKTU":
                print(datetime.datetime.now())

            elif c == "SIAPA":
                print(f"{user} ({role})")

            elif c == "INFO_SAWIT":
                for k, v in system.items():
                    print(f"{k}: {v}")

            elif c == "NEOFETCH":
                print(Fore.GREEN + "   🌴 SaWiTOS")
                print(Fore.WHITE + f"   OS      : {system['os']}")
                print(f"   Kernel  : {system['kernel']}")
                print(f"   User    : {user}")
                print(f"   Shell   : SawitShell")
                print(f"   Time    : {datetime.datetime.now()}")

            elif c == "RIWAYAT":
                for i, h in enumerate(history):
                    print(i, h)

            elif c == "SU":
                u = input("User: ")
                p = getpass.getpass("Password: ")
                if u in users and users[u]["password"] == p:
                    user = u
                    role = users[u]["role"]
                    print("Login berhasil")

            elif c == "SUDO":
                print("Gunakan SU untuk login pejabat")

            elif c == "BANTUAN":
                for k, v in COMMANDS.items():
                    print(f"{Fore.CYAN}{k:<12}{Fore.WHITE} : {v}")

            elif c in ["EXIT", "PULANG"]:
                save(FS_FILE, fs)
                save(USER_FILE, users)
                print(Fore.GREEN + "Keluar dari SaWiTOS 🌴")
                break

            elif c == "SAWIT":
                print(Fore.GREEN + "🌴 Sawit adalah masa depan bangsa 🌴")

            else:
                print(Fore.RED + "Command tidak dikenal")

        except Exception as e:
            print(Fore.RED + f"Error: {e}")

# ===============================
shell()
