import os
import datetime
from filesystem import fs, get_dir, pwd, cd, save_fs

def help_cmd():
    print("""
Commands:
 ls               list files
 cd <dir>         change directory
 pwd              show current path
 touch <file>     create file
 mkdir <dir>      create directory
 rm <name>        remove file or directory
 cat <file>       show file content
 echo <text> > f  write to file
 nano <file>      edit file
 clear            clear screen
 whoami           show user
 time             current time
 help             show this help
 exit             shutdown OS
""")

def nano(file):
    d = get_dir()
    print("Nano editor (CTRL+Z + ENTER to save)")
    lines = []
    try:
        while True:
            lines.append(input())
    except EOFError:
        d[file] = "\n".join(lines)
        save_fs(fs)
        print("[ saved ]")

def shell(user):
    while True:
        try:
            cmd = input(f"{user}@nugra21os:{pwd()}$ ").strip()
        except KeyboardInterrupt:
            print()
            continue

        if not cmd:
            continue

        if cmd == "help":
            help_cmd()

        elif cmd == "ls":
            print("  ".join(get_dir().keys()))

        elif cmd.startswith("cd "):
            if not cd(cmd.split(" ", 1)[1]):
                print("cd: no such directory")

        elif cmd == "pwd":
            print(pwd())

        elif cmd.startswith("touch "):
            get_dir()[cmd.split(" ", 1)[1]] = ""
            save_fs(fs)

        elif cmd.startswith("mkdir "):
            get_dir()[cmd.split(" ", 1)[1]] = {}
            save_fs(fs)

        elif cmd.startswith("rm "):
            get_dir().pop(cmd.split(" ", 1)[1], None)
            save_fs(fs)

        elif cmd.startswith("cat "):
            f = cmd.split(" ", 1)[1]
            print(get_dir().get(f, "file not found"))

        elif cmd.startswith("echo ") and ">" in cmd:
            text, file = cmd.split(">", 1)
            get_dir()[file.strip()] = text.replace("echo", "").strip()
            save_fs(fs)

        elif cmd.startswith("nano "):
            nano(cmd.split(" ", 1)[1])

        elif cmd == "clear":
            os.system("cls" if os.name == "nt" else "clear")

        elif cmd == "whoami":
            print(user)

        elif cmd == "time":
            print(datetime.datetime.now())

        elif cmd == "exit":
            print("Shutting down Nugra21OS...")
            break

        else:
            print("command not found")
