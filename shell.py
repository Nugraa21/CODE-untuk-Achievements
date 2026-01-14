from commands import *
from colorama import Fore, Style

def shell(user):
    cwd = "/home/nugra"

    while True:
        cmd = input(Fore.GREEN + f"{user}@sawitos:{cwd}$ " + Style.RESET_ALL)
        a = cmd.split()

        if not a: continue

        try:
            if a[0] == "LIHAT": LIHAT(cwd)
            elif a[0] == "MASUK": cwd = MASUK(cwd, a[1])
            elif a[0] == "MUNDUR": cwd = MUNDUR(cwd)
            elif a[0] == "POSISI": POSISI(cwd)
            elif a[0] == "BUKA": BUKA(cwd, a[1])
            elif a[0] == "BAKAR": BAKAR(cwd, a[1])
            elif a[0] == "TANAM": TANAM(cwd, a[1])
            elif a[0] == "PANEN": PANEN(cwd, a[1])
            elif a[0] == "RAWAT": RAWAT(cwd, a[1])
            elif a[0] == "TEBANG": TEBANG(cwd, a[1])
            elif a[0] == "CANGKOK": CANGKOK(cwd, a[1], a[2])
            elif a[0] == "SIAPA": SIAPA(user)
            elif a[0] == "INFO_SAWIT": INFO_SAWIT()
            elif a[0] == "BANTUAN": BANTUAN()
            elif a[0] == "SAWIT": print("🔥 MODE SAWIT AKTIF")
            elif a[0] == "PULANG": break
            else: print("Perintah Sawit tidak dikenal")
        except:
            print("Kesalahan perintah")
