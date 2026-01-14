import os
import datetime
from colorama import Fore, init
from filesystem import get_dir, pwd, current_path
from data.files import ASCII_LOGO

init(autoreset=True)

def help_cmd():
    print("""
Available commands:
 help        show this help
 ls          list directory
 cd <dir>    change directory
 cat <file>  read file
 echo <msg>  print message
 clear       clear terminal
 neofetch   system info
 whoami     current user
 time       show time
 exit       shutdown OS
""")

def shell_loop():
    while True:
        cmd = input(Fore.CYAN + f"nugra@nugra21os:{pwd()}$ ").strip()
        args = cmd.split()

        if not args:
            continue

        if args[0] == "help":
            help_cmd()

        elif args[0] == "ls":
            print("  ".join(get_dir().keys()))

        elif args[0] == "cd":
            if len(args) < 2:
                print("cd: missing argument")
            elif args[1] == "..":
                if len(current_path) > 1:
                    current_path.pop()
            elif args[1] in get_dir():
                if isinstance(get_dir()[args[1]], dict):
                    current_path.append(args[1])
                else:
                    print("cd: not a directory")
            else:
                print("cd: no such directory")

        elif args[0] == "cat":
            if len(args) < 2:
                print("cat: missing file")
            elif args[1] in get_dir():
                print(get_dir()[args[1]])
            else:
                print("cat: file not found")

        elif args[0] == "echo":
            print(" ".join(args[1:]))

        elif args[0] == "clear":
            os.system("cls" if os.name == "nt" else "clear")

        elif args[0] == "neofetch":
            print(ASCII_LOGO)
            print("OS      : Nugra21OS")
            print("Kernel  : Python")
            print("Shell   : nugra-shell")
            print("User    : nugra")

        elif args[0] == "whoami":
            print("nugra")

        elif args[0] == "time":
            print(datetime.datetime.now())

        elif args[0] == "exit":
            print("Shutting down Nugra21OS...")
            break

        else:
            print(f"{args[0]}: command not found")
