from colorama import Fore, Style, init
import os, datetime, time, random
init(autoreset=True)

# ===============================
# BERSIHKAN LAYAR (ANSI halus)
# ===============================
def clear():
    os.system("cls" if os.name == "nt" else "clear")
    if os.name != "nt":
        print("\033[?25h", end="")  # Tampilkan kursor

# ===============================
# ANIMASI LOADING (spinner bersih)
# ===============================
def loading_message(msg, duration=1.5):
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\r{Fore.GREEN}{chars[i % len(chars)]}{Style.RESET_ALL} {msg}...", end="", flush=True)
        time.sleep(0.1)
        i += 1
    print(f"\r{Fore.GREEN}OK: {msg} selesai.{Style.RESET_ALL}")

# ===============================
# BANNER / SELAMAT DATANG (garis sederhana, tanpa kotak)
# ===============================
def banner():
    clear()
    quotes = [
        "Sawit: Tanam kode, panen masa depan.",
        "CLI Modular. Berbasis Python. Edisi Nugra21.",
        "Terminal Pro: LS/LIHAT. SUDO. IRIGASI & lainnya."
    ]
    quote = random.choice(quotes)
    print(Fore.CYAN + Style.BRIGHT + "SaWiT OS v1.1 - Terminal Nugra21" + Style.RESET_ALL)
    print(Fore.YELLOW + quote + Style.RESET_ALL)
    print(Fore.WHITE + "BANTUAN: Daftar perintah | NEOFETCH: Info sistem" + Style.RESET_ALL)
    print(Fore.MAGENTA + "=" * 50 + Style.RESET_ALL)  # Pemisah sederhana

# ===============================
# PROMPT TERMINAL (teks role bersih, tanpa ikon)
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
# NEOFETCH (garis kunci-nilai sederhana, tanpa kotak)
# ===============================
def neofetch(system, user, fs_stats, uptime, role):
    print(Fore.GREEN + Style.BRIGHT + "Dasbor SaWiT OS" + Style.RESET_ALL)
    print(Fore.CYAN + "Sistem Operasi : " + Fore.WHITE + system.get("os", "-") + Style.RESET_ALL)
    print(Fore.CYAN + "Kernel         : " + Fore.WHITE + system.get("kernel", "-") + Style.RESET_ALL)
    print(Fore.CYAN + "Waktu Aktif    : " + Fore.WHITE + uptime + Style.RESET_ALL)
    print(Fore.CYAN + "Pengguna       : " + Fore.WHITE + f"{user} ({role})" + Style.RESET_ALL)
    print(Fore.CYAN + "Stat FS        : " + Fore.WHITE + f"{fs_stats['total_files']} file | {fs_stats['total_size']} karakter" + Style.RESET_ALL)
    print(Fore.CYAN + "Waktu          : " + Fore.WHITE + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + Style.RESET_ALL)
    print(Fore.GREEN + "\nTips: Gunakan LS untuk daftar berwarna. Tetap bersih." + Style.RESET_ALL)