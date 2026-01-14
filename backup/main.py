import os
from colorama import Fore, Style, init
from banner import show_banner
from utils import log_activity, pause

init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    print(Fore.CYAN + "1. System Info")
    print(Fore.CYAN + "2. Write Experiment Log")
    print(Fore.CYAN + "3. View Lab Logs")
    print(Fore.CYAN + "4. About Nugra21 Lab")
    print(Fore.RED  + "0. Exit Lab")

def system_info():
    print(Fore.GREEN + "\n🖥 System Information")
    print("-" * 30)
    print(f"OS      : {os.name}")
    print(f"User    : {os.getenv('USERNAME') or os.getenv('USER')}")
    print(f"Path    : {os.getcwd()}")
    log_activity("Checked system information")

def write_log():
    msg = input("Write your experiment note: ")
    log_activity(msg)
    print(Fore.YELLOW + "✔ Log saved to Nugra21 Lab.")

def view_logs():
    print(Fore.MAGENTA + "\n📜 Nugra21 Lab Logs\n")
    try:
        with open("data/logs.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No lab logs found.")

def about():
    print(Fore.BLUE + """
🧪 Nugra21 Lab
Version : 1.0.0
Author  : Nugra21

A free experimental Python lab.
No rules. No pressure.
Just build, test, break, and learn.
""")

def main():
    log_activity("Lab session started")
    while True:
        clear()
        show_banner()
        menu()
        choice = input("\nSelect option: ")

        if choice == "1":
            system_info()
        elif choice == "2":
            write_log()
        elif choice == "3":
            view_logs()
        elif choice == "4":
            about()
        elif choice == "0":
            log_activity("Exited Nugra21 Lab")
            print("👋 Leaving Nugra21 Lab. See you!")
            break
        else:
            print("❌ Invalid option!")

        pause()

if __name__ == "__main__":
    main()
