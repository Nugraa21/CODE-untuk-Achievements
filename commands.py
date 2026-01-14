from filesystem import *
from helpdata import HELP
import os, copy

def LIHAT(cwd):
    fs = load_fs()
    for i in get_dir(fs, cwd):
        print(i)

def MASUK(cwd, name):
    return "/" + "/".join((cwd+"/"+name).split("/")[1:])

def MUNDUR(cwd):
    return "/" + "/".join(cwd.split("/")[:-1])

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
    print(get_dir(fs, cwd).get(name, "File tidak ada"))

def RAWAT(cwd, name):
    fs = load_fs()
    print("Ketik isi (:simpan untuk keluar)")
    isi = []
    while True:
        x = input()
        if x == ":simpan":
            break
        isi.append(x)
    get_dir(fs, cwd)[name] = "\n".join(isi)
    save_fs(fs)

def TEBANG(cwd, name):
    fs = load_fs()
    del get_dir(fs, cwd)[name]
    save_fs(fs)

def CANGKOK(cwd, src, dst):
    fs = load_fs()
    get_dir(fs, cwd)[dst] = copy.deepcopy(get_dir(fs, cwd)[src])
    save_fs(fs)

def SIAPA(user):
    print(user)

def INFO_SAWIT():
    print("🌴 Nugra21 SawitOS v2 | Python Terminal OS")

def BANTUAN():
    for k,v in HELP.items():
        print(f"{k:<12} : {v}")
