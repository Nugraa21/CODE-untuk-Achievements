from filesystem import *
from helpdata import HELP
import os, copy

def LIHAT(cwd):
    fs = load_fs()
    for k in get_dir(fs, cwd):
        print(k)

def MASUK(cwd, name):
    if name == "..":
        return "/" + "/".join(cwd.split("/")[:-1])
    return cwd.rstrip("/") + "/" + name

def POSISI(cwd):
    print(cwd)

def BUKA(cwd, name):
    fs = load_fs()
    get_dir(fs, cwd)[name] = {}
    save_fs(fs)

def BAKAR(cwd, name):
    fs = load_fs()
    del get_dir(fs, cwd)[name]
    save_fs(fs)

def TANAM(cwd, name):
    fs = load_fs()
    get_dir(fs, cwd)[name] = ""
    save_fs(fs)

def PANEN(cwd, name):
    fs = load_fs()
    print(get_dir(fs, cwd).get(name, "File tidak ditemukan"))

def RAWAT(cwd, name):
    fs = load_fs()
    print("Edit file (:simpan untuk keluar)")
    data = []
    while True:
        x = input()
        if x == ":simpan":
            break
        data.append(x)
    get_dir(fs, cwd)[name] = "\n".join(data)
    save_fs(fs)

def TEBANG(cwd, name):
    fs = load_fs()
    del get_dir(fs, cwd)[name]
    save_fs(fs)

def CANGKOK(cwd, src, dst):
    fs = load_fs()
    get_dir(fs, cwd)[dst] = copy.deepcopy(get_dir(fs, cwd)[src])
    save_fs(fs)

def PINDAH(cwd, src, dst):
    fs = load_fs()
    get_dir(fs, cwd)[dst] = get_dir(fs, cwd)[src]
    del get_dir(fs, cwd)[src]
    save_fs(fs)

def BERSIHKAN():
    os.system("cls" if os.name == "nt" else "clear")

def SIAPA(user):
    print(user)

def INFO_SAWIT():
    print("🌴 Nugra21.SaWiTOS v3 | Python Terminal OS")

def BANTUAN():
    for k,v in HELP.items():
        print(f"{k:<12} : {v}")
