from ui import *
from commands import tree
from auth import hash_password
import datetime
import getpass

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
    "PINDAH": "Pindah/rename file/folder (lengkap: PINDAH sumber tujuan)",
    "IRIGASI": "Cari file/folder",
    "BERSIHKAN": "Bersihkan layar",
    "CLS": "Alias bersihkan",
    "WAKTU": "Waktu saat ini",
    "SIAPA": "Pengguna dan peran saat ini",
    "INFO_SAWIT": "Info sistem dasar",
    "NEOFETCH": "Info sistem detail",
    "SUDO": "Ganti ke mode PEJABAT (pw admin123)",
    "RAKYAT": "Kembali ke mode RAKYAT (alias UNSU)",
    "UNSU": "Alias RAKYAT - Keluar mode PEJABAT",
    "BANTUAN": "Daftar perintah",
    "SAWIT": "Telur Paskah",
    "HISTORY": "Riwayat perintah (10 terakhir)",
    "EXIT": "Keluar OS",
    "PULANG": "Alias keluar"
}

def shell(fs, users, system, save_fs):
    user = "nugra"  # Default user "nugra" biar match FS
    role = users[user]["role"]
    cwd = ["/"]  # Mulai di root
    history = []
    uptime_start = datetime.datetime.now()

    def curdir():
        d = fs["/"]  # Selalu mulai dari root
        for p in cwd[1:]:  # Lewati "/", navigasi sisanya
            d = d[p]
        return d

    def pwd():
        return "/" if len(cwd) == 1 else "/".join(cwd)

    def get_fs_stats():
        def count_items(d, total_files=0, total_size=0):
            for k, v in d.items():
                if isinstance(v, str):
                    total_files += 1
                    total_size += len(v)
                elif isinstance(v, dict):
                    total_files, total_size = count_items(v, total_files, total_size)
            return total_files, total_size
        return {"total_files": count_items(fs["/"])[0], "total_size": count_items(fs["/"])[1]}

    # cd awal ke home/nugra jika ada
    if "home" in fs["/"] and "nugra" in fs["/"]["home"]:
        cwd = ["/", "home", "nugra"]

    banner()

    while True:
        cmd = input(prompt(user, role, pwd())).strip()
        history.append(cmd)
        if not cmd:
            continue
        a = cmd.split()
        c = a[0].upper()

        try:
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
                        size = "dir"
                        print(Fore.CYAN + f"  [DIR] {k:<20} {Fore.WHITE}{size:<8} folder{Style.RESET_ALL}")
                    else:
                        size = len(v) if isinstance(v, str) else "0"
                        print(Fore.GREEN + f"  [FILE] {k:<20} {Fore.WHITE}{size} karakter  file{Style.RESET_ALL}")
                print(Fore.LIGHTBLACK_EX + f"Total: {total} item" + Style.RESET_ALL)

            elif c == "MASUK":
                if len(a) < 2:
                    print(Fore.RED + Style.BRIGHT + "KESALAHAN: Masukkan nama folder!" + Style.RESET_ALL)
                    continue
                if a[1] in curdir() and isinstance(curdir()[a[1]], dict):
                    cwd.append(a[1])
                    print(Fore.GREEN + Style.BRIGHT + f"BERHASIL: Masuk ke {a[1]}." + Style.RESET_ALL)
                else:
                    print(Fore.RED + Style.BRIGHT + "KESALAHAN: Folder tidak ditemukan: " + Fore.YELLOW + a[1] + Style.RESET_ALL)

            elif c == "MUNDUR":
                if len(cwd) > 1:
                    cwd.pop()
                    print(Fore.GREEN + Style.BRIGHT + f"BERHASIL: Kembali ke {pwd()}." + Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + "Sudah di root." + Style.RESET_ALL)

            elif c == "POSISI":
                print(Fore.YELLOW + Style.BRIGHT + pwd() + Style.RESET_ALL)

            elif c == "BUKA":
                if len(a) < 2:
                    print(Fore.RED + "KESALAHAN: Masukkan nama folder!" + Style.RESET_ALL)
                    continue
                if a[1] in curdir():
                    print(Fore.YELLOW + "PERINGATAN: Folder sudah ada." + Style.RESET_ALL)
                else:
                    curdir()[a[1]] = {}
                    print(Fore.GREEN + f"BERHASIL: Folder '{a[1]}' dibuat." + Style.RESET_ALL)
                    save_fs(fs)

            elif c == "BAKAR":
                if len(a) < 2:
                    print(Fore.RED + "KESALAHAN: Masukkan nama folder!" + Style.RESET_ALL)
                    continue
                if role != "pejabat":
                    print(Fore.RED + "KESALAHAN: Mode PEJABAT diperlukan." + Style.RESET_ALL)
                elif a[1] in curdir():
                    del curdir()[a[1]]
                    print(Fore.RED + f"BERHASIL: Folder '{a[1]}' dihapus." + Style.RESET_ALL)
                    save_fs(fs)
                else:
                    print(Fore.RED + "KESALAHAN: Folder tidak ditemukan." + Style.RESET_ALL)

            elif c == "KEBUN":
                tree(curdir())

            elif c == "TANAM":
                if len(a) < 2:
                    print(Fore.RED + "KESALAHAN: Masukkan nama file!" + Style.RESET_ALL)
                    continue
                if a[1] in curdir():
                    print(Fore.YELLOW + "PERINGATAN: File sudah ada." + Style.RESET_ALL)
                else:
                    curdir()[a[1]] = ""
                    print(Fore.GREEN + f"BERHASIL: File '{a[1]}' dibuat." + Style.RESET_ALL)
                    save_fs(fs)

            elif c == "PANEN":
                if len(a) < 2:
                    print(Fore.RED + "KESALAHAN: Masukkan nama file!" + Style.RESET_ALL)
                    continue
                if a[1] in curdir() and isinstance(curdir()[a[1]], str):
                    print(Fore.CYAN + Style.BRIGHT + f"Isi '{a[1]}':" + Style.RESET_ALL)
                    print(Fore.WHITE + curdir()[a[1]] + Style.RESET_ALL)
                else:
                    print(Fore.RED + "KESALAHAN: File tidak ditemukan." + Style.RESET_ALL)

            elif c == "RAWAT":
                if len(a) < 2:
                    print(Fore.RED + "KESALAHAN: Masukkan nama file!" + Style.RESET_ALL)
                    continue
                if a[1] not in curdir() or not isinstance(curdir()[a[1]], str):
                    print(Fore.RED + "KESALAHAN: File tidak valid." + Style.RESET_ALL)
                    continue
                print(Fore.YELLOW + f"Edit '{a[1]}' (:simpan untuk simpan, :keluar untuk batal)" + Style.RESET_ALL)
                isi = curdir()[a[1]].split('\n')
                while True:
                    l = input(Fore.GREEN + ">> " + Style.RESET_ALL)
                    if l == ":simpan":
                        curdir()[a[1]] = "\n".join(isi)
                        print(Fore.GREEN + "BERHASIL: Disimpan." + Style.RESET_ALL)
                        save_fs(fs)
                        break
                    elif l == ":keluar":
                        print(Fore.YELLOW + "Edit dibatalkan." + Style.RESET_ALL)
                        break
                    else:
                        isi.append(l)

            elif c == "TEBANG":
                if len(a) < 2:
                    print(Fore.RED + "KESALAHAN: Masukkan nama!" + Style.RESET_ALL)
                    continue
                if a[1] in curdir():
                    del curdir()[a[1]]
                    print(Fore.RED + f"BERHASIL: '{a[1]}' dihapus." + Style.RESET_ALL)
                    save_fs(fs)
                else:
                    print(Fore.RED + "KESALAHAN: Tidak ditemukan." + Style.RESET_ALL)

            elif c == "CANGKOK":
                if len(a) < 3:
                    print(Fore.RED + "KESALAHAN: CANGKOK sumber tujuan" + Style.RESET_ALL)
                    continue
                src, dest = a[1], a[2]
                if src in curdir() and isinstance(curdir()[src], str):
                    curdir()[dest] = curdir()[src]
                    print(Fore.GREEN + f"BERHASIL: '{src}' disalin ke '{dest}'." + Style.RESET_ALL)
                    save_fs(fs)
                else:
                    print(Fore.RED + "KESALAHAN: Sumber tidak valid." + Style.RESET_ALL)

            # PINDAH lengkap: Pindah/rename file atau folder (seperti mv di Linux)
            elif c == "PINDAH":
                if len(a) < 3:
                    print(Fore.RED + "KESALAHAN: Gunakan PINDAH sumber tujuan (misal: PINDAH file.txt newfile.txt)" + Style.RESET_ALL)
                    continue
                src = a[1]
                dest = a[2]
                if src not in curdir():
                    print(Fore.RED + "KESALAHAN: Sumber tidak ditemukan." + Style.RESET_ALL)
                    continue
                if dest in curdir():
                    print(Fore.YELLOW + "PERINGATAN: Tujuan sudah ada. Overwrite? (y/n)" + Style.RESET_ALL)
                    confirm = input().strip().lower()
                    if confirm != 'y':
                        print(Fore.YELLOW + "Pindah dibatalkan." + Style.RESET_ALL)
                        continue
                curdir()[dest] = curdir().pop(src)
                print(Fore.GREEN + f"BERHASIL: '{src}' dipindah/rename ke '{dest}'." + Style.RESET_ALL)
                save_fs(fs)

            elif c == "IRIGASI":
                if len(a) < 2:
                    print(Fore.RED + "KESALAHAN: IRIGASI kata kunci" + Style.RESET_ALL)
                    continue
                keyword = a[1].lower()
                def search(d, path=""):
                    results = []
                    for k, v in d.items():
                        if keyword in k.lower():
                            results.append(path + "/" + k)
                        if isinstance(v, dict):
                            results.extend(search(v, path + "/" + k))
                        elif isinstance(v, str) and keyword in v.lower():
                            results.append(path + "/" + k + " (isi)")
                    return results
                found = search(fs["/"])
                if found:
                    print(Fore.GREEN + "Hasil pencarian:" + Style.RESET_ALL)
                    for f in found:
                        print(Fore.WHITE + f"  {f}" + Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + "Tidak ada hasil." + Style.RESET_ALL)

            elif c in ["BERSIHKAN", "CLS"]:
                banner()

            elif c == "WAKTU":
                print(Fore.MAGENTA + Style.BRIGHT + str(datetime.datetime.now()) + Style.RESET_ALL)

            elif c == "SIAPA":
                print(Fore.CYAN + f"{user} ({role})" + Style.RESET_ALL)

            elif c == "INFO_SAWIT":
                for k, v in system.items():
                    print(Fore.CYAN + f"{k}: " + Fore.WHITE + str(v) + Style.RESET_ALL)

            elif c == "NEOFETCH":
                uptime = str(datetime.datetime.now() - uptime_start).split('.')[0]
                neofetch(system, user, get_fs_stats(), uptime, role)

            # SUDO: Ganti ke PEJABAT, pw "admin123"
            elif c == "SUDO":
                if role == "pejabat":
                    print(Fore.YELLOW + "Sudah di mode PEJABAT." + Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + f"[sudo] password untuk {user}:" + Style.RESET_ALL)
                    sudo_pass = getpass.getpass()
                    user_hashed = users.get(user, {}).get("password", "")
                    if hash_password(sudo_pass) == user_hashed:
                        role = "pejabat"
                        print(Fore.RED + "BERHASIL: Mode PEJABAT diaktifkan. Gunakan dengan hati-hati." + Style.RESET_ALL)
                    else:
                        print(Fore.RED + "KESALAHAN: Maaf, coba lagi." + Style.RESET_ALL)

            # RAKYAT/UNSU: Kembali ke RAKYAT
            elif c in ["RAKYAT", "UNSU"]:
                if role == "rakyat":
                    print(Fore.YELLOW + "Sudah di mode RAKYAT." + Style.RESET_ALL)
                else:
                    role = "rakyat"
                    print(Fore.GREEN + "BERHASIL: Kembali ke mode RAKYAT." + Style.RESET_ALL)

            elif c == "BANTUAN":
                print(Fore.CYAN + Style.BRIGHT + "\nPerintah SaWiT:" + Style.RESET_ALL)
                for k, v in sorted(COMMANDS.items()):
                    print(Fore.WHITE + f"{Fore.YELLOW}{k:<12}{Fore.WHITE} : {v}" + Style.RESET_ALL)

            elif c == "HISTORY":
                print(Fore.CYAN + f"\n10 Perintah Terakhir ({len(history)} total):" + Style.RESET_ALL)
                for i, h in enumerate(history[-10:], 1):
                    print(Fore.WHITE + f"  {i:2d}. {Fore.LIGHTBLACK_EX}{h}{Style.RESET_ALL}")

            elif c in ["EXIT", "PULANG"]:
                loading_message("Menyimpan FS & pembersihan")
                save_fs(fs)
                print(Fore.GREEN + Style.BRIGHT + "\nPemadaman: Selamat tinggal." + Style.RESET_ALL)
                break

            elif c == "SAWIT":
                print(Fore.YELLOW + "Sawit adalah masa depan. Terus berkembang." + Style.RESET_ALL)

            else:
                print(Fore.RED + Style.BRIGHT + f"KESALAHAN: Perintah '{c}' tidak dikenal. Periksa BANTUAN." + Style.RESET_ALL)

        except KeyError as e:
            print(Fore.RED + Style.BRIGHT + f"KESALAHAN: Path tidak ditemukan - {e}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + Style.BRIGHT + f"KESALAHAN: {e}. Coba lagi?" + Style.RESET_ALL)