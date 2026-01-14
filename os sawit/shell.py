from commands import *
from colorama import Fore, Style, init
init()

def shell(user):
    cwd = "/home/nugra"

    while True:
        prompt = (
            Fore.GREEN + user +
            Fore.WHITE + "@"+
            Fore.YELLOW + "Nugra21.SaWiTOS" +
            Fore.WHITE + ":" +
            Fore.CYAN + cwd +
            Fore.WHITE + "$ " +
            Style.RESET_ALL
        )

        cmd = input(prompt).strip()
        if not cmd:
            continue

        a = cmd.split()

        # Alias Linux
        if a[0] == "ls": a[0] = "LIHAT"
        if a[0] == "cd": a[0] = "MASUK"
        if a[0] == "clear": a[0] = "BERSIHKAN"
        if a[0] == "exit": a[0] = "PULANG"

        try:
            if a[0] == "LIHAT": LIHAT(cwd)
            elif a[0] == "MASUK": cwd = MASUK(cwd, a[1])
            elif a[0] == "MUNDUR": cwd = MASUK(cwd, "..")
            elif a[0] == "POSISI": POSISI(cwd)
            elif a[0] == "BUKA": BUKA(cwd, a[1])
            elif a[0] == "BAKAR": BAKAR(cwd, a[1])
            elif a[0] == "TANAM": TANAM(cwd, a[1])
            elif a[0] == "PANEN": PANEN(cwd, a[1])
            elif a[0] == "RAWAT": RAWAT(cwd, a[1])
            elif a[0] == "TEBANG": TEBANG(cwd, a[1])
            elif a[0] == "CANGKOK": CANGKOK(cwd, a[1], a[2])
            elif a[0] == "PINDAH": PINDAH(cwd, a[1], a[2])
            elif a[0] == "BERSIHKAN": BERSIHKAN()
            elif a[0] == "SIAPA": SIAPA(user)
            elif a[0] == "INFO_SAWIT": INFO_SAWIT()
            elif a[0] == "BANTUAN": BANTUAN()
            elif a[0] == "SAWIT": print("🔥 MODE SAWIT AKTIF 🌴")
            elif a[0] == "PULANG": break
            else:
                print("Perintah tidak dikenali. Ketik BANTUAN.")
        except:
            print("Kesalahan penggunaan command")
