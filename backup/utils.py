from datetime import datetime

LOG_FILE = "data/logs.txt"

def log_activity(message):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as file:
        file.write(f"[NUGRA21 LAB | {time}] {message}\n")

def pause():
    input("\nPress ENTER to continue...")
