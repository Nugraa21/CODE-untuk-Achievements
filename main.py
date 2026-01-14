# SaWiT OS v1.1 - Terminal Nugra21 (versi single-file + penyimpanan permanen)
# Creator: Ludang Prasetyo Nugroho

from colorama import Fore, Style, init
import os
import datetime
import time
import random
import getpass
import hashlib
import json

init(autoreset=True)

# Lokasi penyimpanan data
DATA_DIR = "data"
FS_FILE = os.path.join(DATA_DIR, "sawit_fs.json")

# ===============================
# Fungsi clear layar
# ===============================
def clear():
    os.system("cls" if os.name == "nt" else "clear")
    if os.name != "nt":
        print("\033[?25h", end="")

# ===============================
# Loading animasi
# ===============================
def loading_message(msg, duration=1.2):
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\r{Fore.GREEN}{chars[i % len(chars)]}{Style.RESET_ALL} {msg}...", end="", flush=True)
        time.sleep(0.1)
        i += 1
    print(f"\r{Fore.GREEN}OK: {msg} selesai.{Style.RESET_ALL}")

# ===============================
# Banner
# ===============================
def banner():
    clear()
    quotes = [
        "--------------------------------"
        # "CLI Modular. Berbasis Python. Edisi Nugra21."
        # "Terminal Pro: LS/LIHAT. SUDO. IRIGASI & lainnya."
    ]
    quote = random.choice(quotes)
    print(Fore.CYAN + Style.BRIGHT + "SaWiT OS v1.1 - Terminal Nugra21" + Style.RESET_ALL)
    print(Fore.YELLOW + quote + Style.RESET_ALL)
    # print(Fore.WHITE + "BANTUAN: Daftar perintah | NEOFETCH: Info sistem" + Style.RESET_ALL)
    # print(Fore.MAGENTA + "=" * 50 + Style.RESET_ALL)

# ===============================
# Prompt
# ===============================
def prompt(user, role, path):
    now = datetime.datetime.now().strftime("%H:%M")
    branch = "dev" if "projects" in path else "main"
    branch_color = Fore.MAGENTA if branch == "dev" else Fore.YELLOW
    role_text = "PEJABAT" if role == "pejabat" else "RAKYAT"
    return (
        Fore.CYAN + Style.BRIGHT + user + Fore.WHITE + "@" + Fore.GREEN + "sawit" +
        Fore.WHITE + f":{Fore.YELLOW}{path}{Fore.WHITE}] " +
        branch_color + f"({branch})" + Fore.WHITE + " " +
        Fore.MAGENTA + now + Fore.WHITE + " " + Fore.CYAN + role_text +
        Fore.WHITE + Style.BRIGHT + " -> " + Style.RESET_ALL
    )

# ===============================
# Neofetch
# ===============================
def neofetch(system, user, fs_stats, uptime, role):
    print(Fore.GREEN + Style.BRIGHT + "Dasbor SaWiT OS" + Style.RESET_ALL)
    print(Fore.CYAN + "Sistem Operasi : " + Fore.WHITE + system.get("os", "-") + Style.RESET_ALL)
    print(Fore.CYAN + "Kernel         : " + Fore.WHITE + system.get("kernel", "-") + Style.RESET_ALL)
    print(Fore.CYAN + "Waktu Aktif    : " + Fore.WHITE + uptime + Style.RESET_ALL)
    print(Fore.CYAN + "Pengguna       : " + Fore.WHITE + f"{user} ({role})" + Style.RESET_ALL)
    print(Fore.CYAN + "Stat FS        : " + Fore.WHITE + f"{fs_stats['total_files']} file | {fs_stats['total_size']} karakter" + Style.RESET_ALL)
    print(Fore.CYAN + "Waktu          : " + Fore.WHITE + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + Style.RESET_ALL)
    print(Fore.GREEN + "\nTips: Gunakan LS untuk daftar berwarna." + Style.RESET_ALL)

# ===============================
# Tree direktori
# ===============================
def tree(d, pad="", is_last=True):
    keys = list(d.keys())
    for i, k in enumerate(keys):
        v = d[k]
        connector = "└── " if i == len(keys) - 1 else "├── "
        print(pad + Fore.GREEN + connector + Fore.WHITE + k + Style.RESET_ALL)
        if isinstance(v, dict):
            extension = "    " if i == len(keys) - 1 else "│   "
            tree(v, pad + extension)

# ===============================
# Hash password
# ===============================
def hash_password(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

# ===============================
# Load & Save filesystem
# ===============================
def load_filesystem(default_fs):
    os.makedirs(DATA_DIR, exist_ok=True)
    if os.path.exists(FS_FILE):
        try:
            with open(FS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(Fore.RED + f"Gagal memuat data sebelumnya: {e}" + Style.RESET_ALL)
            print(Fore.YELLOW + "Menggunakan struktur default..." + Style.RESET_ALL)
    return default_fs

def save_filesystem(fs):
    try:
        with open(FS_FILE, "w", encoding="utf-8") as f:
            json.dump(fs, f, indent=2, ensure_ascii=False)
        # print(Fore.GREEN + "Data tersimpan." + Style.RESET_ALL)  # uncomment jika mau debug
    except Exception as e:
        print(Fore.RED + f"Gagal menyimpan data: {e}" + Style.RESET_ALL)

# ===============================
# Data default (hanya dipakai pertama kali)
# ===============================
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

DEFAULT_USERS = {
    "nugra": {"password": hash_password("123"), "role": "rakyat"},
    "pejabat": {"password": hash_password("123"), "role": "pejabat"}
}

DEFAULT_SYSTEM = {
    "os": "Nugra21.SaWiT-OS",
    "version": "1.1 SAWIT-ENHANCED",
    "kernel": "SawitKernel v2.0",
    "creator": "Ludang Prasetyo Nugroho",
    "uptime": "Fresh boot"
}

# ===============================
# Daftar perintah
# ===============================
COMMANDS = {
    "LIHAT": "Tampilkan isi direktori (alias LS)",
    "LS": "Alias LIHAT - Daftar berwarna",
    "MASUK": "Masuk direktori",
    "MUNDUR": "Kembali ke direktori induk",
    "POSISI": "Path saat ini (pwd)",
    "BUKA": "Buat folder baru",
    "BAKAR": "Hapus folder (hanya PEJABAT)",
    "KEBUN": "Pohon direktori",
    "TANAM": "Buat file kosong",
    "PANEN": "Baca isi file",
    "RAWAT": "Edit file (:simpan untuk simpan, :keluar untuk batal)",
    "TEBANG": "Hapus file/folder",
    "CANGKOK": "Salin file",
    "PINDAH": "Pindah/rename file/folder (PINDAH sumber tujuan)",
    "IRIGASI": "Cari file/folder",
    "BERSIHKAN": "Bersihkan layar",
    "CLS": "Alias bersihkan",
    "WAKTU": "Waktu saat ini",
    "SIAPA": "Pengguna dan peran saat ini",
    "INFO_SAWIT": "Info sistem dasar",
    "NEOFETCH": "Info sistem detail",
    "SUDO": "Ganti ke mode PEJABAT (pw 123)",
    "RAKYAT": "Kembali ke mode RAKYAT (alias UNSU)",
    "UNSU": "Alias RAKYAT",
    "BANTUAN": "Daftar perintah",
    "SAWIT": "Telur Paskah",
    "HISTORY": "Riwayat perintah (10 terakhir)",
    "EXIT": "Keluar OS",
    "PULANG": "Alias keluar"
}

# ===============================
# Shell utama
# ===============================
def shell(fs, users, system):
    user = "nugra"
    role = users[user]["role"]
    cwd = ["/"]
    history = []
    uptime_start = datetime.datetime.now()

    # Auto masuk ke home/nugra jika ada
    if "home" in fs["/"] and "nugra" in fs["/"]["home"]:
        cwd = ["/", "home", "nugra"]

    def curdir():
        d = fs["/"]
        for p in cwd[1:]:
            if p in d and isinstance(d[p], dict):
                d = d[p]
            else:
                raise KeyError(f"Path rusak: {p}")
        return d

    def pwd():
        return "/" if len(cwd) == 1 else "/".join(cwd)

    def get_fs_stats():
        def count(d):
            files = 0
            size = 0
            for v in d.values():
                if isinstance(v, str):
                    files += 1
                    size += len(v)
                elif isinstance(v, dict):
                    f, s = count(v)
                    files += f
                    size += s
            return files, size
        total_files, total_size = count(fs["/"])
        return {"total_files": total_files, "total_size": total_size}

    banner()

    while True:
        try:
            cmd = input(prompt(user, role, pwd())).strip()
            if not cmd:
                continue
            history.append(cmd)
            parts = cmd.split()
            c = parts[0].upper()

            if c in ["LIHAT", "LS"]:
                items = curdir()
                if not items:
                    print(Fore.YELLOW + "Direktori kosong." + Style.RESET_ALL)
                    continue
                print(Fore.CYAN + Style.BRIGHT + f"\nDIR: {pwd()}" + Style.RESET_ALL)
                total = 0
                for k, v in sorted(items.items()):
                    total += 1
                    if isinstance(v, dict):
                        print(Fore.CYAN + f"  [DIR]  {k:<20} folder" + Style.RESET_ALL)
                    else:
                        sz = len(v) if isinstance(v, str) else 0
                        print(Fore.GREEN + f"  [FILE] {k:<20} {sz} karakter  file" + Style.RESET_ALL)
                print(Fore.LIGHTBLACK_EX + f"Total: {total} item" + Style.RESET_ALL)

            elif c == "MASUK":
                if len(parts) < 2:
                    print(Fore.RED + "Masukkan nama folder" + Style.RESET_ALL)
                    continue
                target = parts[1]
                if target in curdir() and isinstance(curdir()[target], dict):
                    cwd.append(target)
                    print(Fore.GREEN + f"Masuk ke {target}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"Folder tidak ditemukan: {target}" + Style.RESET_ALL)

            elif c == "MUNDUR":
                if len(cwd) > 1:
                    cwd.pop()
                    print(Fore.GREEN + f"Kembali ke {pwd()}" + Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + "Sudah di root" + Style.RESET_ALL)

            elif c == "POSISI":
                print(Fore.YELLOW + pwd() + Style.RESET_ALL)

            elif c == "BUKA":
                if len(parts) < 2:
                    print(Fore.RED + "Masukkan nama folder" + Style.RESET_ALL)
                    continue
                name = parts[1]
                if name in curdir():
                    print(Fore.YELLOW + "Folder sudah ada" + Style.RESET_ALL)
                else:
                    curdir()[name] = {}
                    print(Fore.GREEN + f"Folder '{name}' dibuat" + Style.RESET_ALL)
                    save_filesystem(fs)

            elif c == "BAKAR":
                if role != "pejabat":
                    print(Fore.RED + "Hanya PEJABAT yang boleh" + Style.RESET_ALL)
                    continue
                if len(parts) < 2:
                    print(Fore.RED + "Masukkan nama folder" + Style.RESET_ALL)
                    continue
                name = parts[1]
                if name in curdir() and isinstance(curdir()[name], dict):
                    del curdir()[name]
                    print(Fore.RED + f"Folder '{name}' dihapus" + Style.RESET_ALL)
                    save_filesystem(fs)
                else:
                    print(Fore.RED + "Folder tidak ditemukan" + Style.RESET_ALL)

            elif c == "KEBUN":
                print(Fore.CYAN + f"Pohon direktori: {pwd()}" + Style.RESET_ALL)
                tree(curdir())

            elif c == "TANAM":
                if len(parts) < 2:
                    print(Fore.RED + "Masukkan nama file" + Style.RESET_ALL)
                    continue
                name = parts[1]
                if name in curdir():
                    print(Fore.YELLOW + "File sudah ada" + Style.RESET_ALL)
                else:
                    curdir()[name] = ""
                    print(Fore.GREEN + f"File '{name}' dibuat" + Style.RESET_ALL)
                    save_filesystem(fs)

            elif c == "PANEN":
                if len(parts) < 2:
                    print(Fore.RED + "Masukkan nama file" + Style.RESET_ALL)
                    continue
                name = parts[1]
                if name in curdir() and isinstance(curdir()[name], str):
                    print(Fore.CYAN + f"Isi '{name}':" + Style.RESET_ALL)
                    print(Fore.WHITE + curdir()[name] + Style.RESET_ALL)
                else:
                    print(Fore.RED + "File tidak ditemukan atau bukan file" + Style.RESET_ALL)

            elif c == "RAWAT":
                if len(parts) < 2:
                    print(Fore.RED + "Masukkan nama file" + Style.RESET_ALL)
                    continue
                name = parts[1]
                if name not in curdir() or not isinstance(curdir()[name], str):
                    print(Fore.RED + "File tidak valid" + Style.RESET_ALL)
                    continue
                print(Fore.YELLOW + f"Edit '{name}'  (:simpan / :keluar)" + Style.RESET_ALL)
                lines = curdir()[name].splitlines()
                while True:
                    line = input(Fore.GREEN + ">> " + Style.RESET_ALL)
                    if line == ":simpan":
                        curdir()[name] = "\n".join(lines)
                        print(Fore.GREEN + "Disimpan" + Style.RESET_ALL)
                        save_filesystem(fs)
                        break
                    elif line == ":keluar":
                        print(Fore.YELLOW + "Dibatalkan" + Style.RESET_ALL)
                        break
                    else:
                        lines.append(line)

            elif c == "TEBANG":
                if len(parts) < 2:
                    print(Fore.RED + "Masukkan nama" + Style.RESET_ALL)
                    continue
                name = parts[1]
                if name in curdir():
                    del curdir()[name]
                    print(Fore.RED + f"'{name}' dihapus" + Style.RESET_ALL)
                    save_filesystem(fs)
                else:
                    print(Fore.RED + "Tidak ditemukan" + Style.RESET_ALL)

            elif c == "CANGKOK":
                if len(parts) < 3:
                    print(Fore.RED + "CANGKOK sumber tujuan" + Style.RESET_ALL)
                    continue
                src, dest = parts[1], parts[2]
                if src in curdir() and isinstance(curdir()[src], str):
                    curdir()[dest] = curdir()[src]
                    print(Fore.GREEN + f"'{src}' disalin ke '{dest}'" + Style.RESET_ALL)
                    save_filesystem(fs)
                else:
                    print(Fore.RED + "Sumber tidak valid" + Style.RESET_ALL)

            elif c == "PINDAH":
                if len(parts) < 3:
                    print(Fore.RED + "PINDAH sumber tujuan" + Style.RESET_ALL)
                    continue
                src, dest = parts[1], parts[2]
                if src not in curdir():
                    print(Fore.RED + "Sumber tidak ditemukan" + Style.RESET_ALL)
                    continue
                if dest in curdir():
                    print(Fore.YELLOW + "Tujuan sudah ada. Overwrite? (y/n)" + Style.RESET_ALL)
                    if input().strip().lower() != "y":
                        print(Fore.YELLOW + "Dibatalkan" + Style.RESET_ALL)
                        continue
                curdir()[dest] = curdir().pop(src)
                print(Fore.GREEN + f"'{src}' dipindah ke '{dest}'" + Style.RESET_ALL)
                save_filesystem(fs)

            elif c == "IRIGASI":
                if len(parts) < 2:
                    print(Fore.RED + "IRIGASI kata_kunci" + Style.RESET_ALL)
                    continue
                keyword = parts[1].lower()
                def cari(d, path=""):
                    hasil = []
                    for k, v in d.items():
                        full = path + "/" + k if path else "/" + k
                        if keyword in k.lower():
                            hasil.append(full)
                        if isinstance(v, dict):
                            hasil.extend(cari(v, full))
                        elif isinstance(v, str) and keyword in v.lower():
                            hasil.append(full + " (di dalam isi)")
                    return hasil
                found = cari(fs["/"])
                if found:
                    print(Fore.GREEN + "Hasil:" + Style.RESET_ALL)
                    for f in found:
                        print("  " + f)
                else:
                    print(Fore.YELLOW + "Tidak ditemukan" + Style.RESET_ALL)

            elif c in ["BERSIHKAN", "CLS"]:
                banner()

            elif c == "WAKTU":
                print(Fore.MAGENTA + str(datetime.datetime.now()) + Style.RESET_ALL)

            elif c == "SIAPA":
                print(Fore.CYAN + f"{user} ({role})" + Style.RESET_ALL)

            elif c == "INFO_SAWIT":
                for k, v in system.items():
                    print(f"{k}: {v}")

            elif c == "NEOFETCH":
                uptime = str(datetime.datetime.now() - uptime_start).split('.')[0]
                neofetch(system, user, get_fs_stats(), uptime, role)

            elif c == "SUDO":
                if role == "pejabat":
                    print(Fore.YELLOW + "Sudah PEJABAT" + Style.RESET_ALL)
                    continue
                print(Fore.YELLOW + f"[sudo] password untuk {user}: ", end="", flush=True)
                pw = getpass.getpass("")
                if hash_password(pw) == users[user]["password"]:
                    role = "pejabat"
                    print(Fore.RED + "Mode PEJABAT diaktifkan" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Password salah" + Style.RESET_ALL)

            elif c in ["RAKYAT", "UNSU"]:
                if role == "rakyat":
                    print(Fore.YELLOW + "Sudah RAKYAT" + Style.RESET_ALL)
                else:
                    role = "rakyat"
                    print(Fore.GREEN + "Kembali ke mode RAKYAT" + Style.RESET_ALL)

            elif c == "BANTUAN":
                print(Fore.CYAN + "\nPerintah SaWiT:" + Style.RESET_ALL)
                for k, v in sorted(COMMANDS.items()):
                    print(f"{Fore.YELLOW}{k:<12}{Fore.WHITE}: {v}")

            elif c == "HISTORY":
                print(Fore.CYAN + f"\n10 terakhir ({len(history)} total):" + Style.RESET_ALL)
                for i, h in enumerate(history[-10:], 1):
                    print(f"  {i:2d}. {h}")

            elif c in ["EXIT", "PULANG"]:
                print(Fore.GREEN + "Menyimpan data..." + Style.RESET_ALL)
                save_filesystem(fs)
                print(Fore.GREEN + "\nPemadaman sistem. Selamat tinggal." + Style.RESET_ALL)
                break

            elif c == "SAWIT":
                print(Fore.YELLOW + "Sawit adalah masa depan. Terus berkembang." + Style.RESET_ALL)

            else:
                print(Fore.RED + f"Perintah tidak dikenal: {c}. Ketik BANTUAN" + Style.RESET_ALL)

        except KeyboardInterrupt:
            print("\n^C")
            print(Fore.GREEN + "Menyimpan data sebelum keluar..." + Style.RESET_ALL)
            save_filesystem(fs)
            break
        except Exception as e:
            print(Fore.RED + f"Error: {str(e)}" + Style.RESET_ALL)

# ===============================
# Mulai program
# ===============================
if __name__ == "__main__":
    print(Fore.CYAN + "Memulai SaWiT OS..." + Style.RESET_ALL)
    loading_message("Memeriksa data penyimpanan")
    fs = load_filesystem(DEFAULT_FS)
    loading_message("Memuat filesystem")
    loading_message("Siap menjalankan terminal")

    shell(fs, DEFAULT_USERS, DEFAULT_SYSTEM)