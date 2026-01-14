import time
from colorama import Fore, init

init(autoreset=True)

def boot_screen():
    print(Fore.GREEN + "Booting Nugra21OS...")
    time.sleep(0.5)
    print(Fore.GREEN + "[ OK ] Loading kernel")
    time.sleep(0.5)
    print(Fore.GREEN + "[ OK ] Mounting filesystem")
    time.sleep(0.5)
    print(Fore.GREEN + "[ OK ] Starting terminal")
    time.sleep(0.5)
    print()
