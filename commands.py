from colorama import Fore, Style

def tree(d, pad="", is_last=True):
    keys = list(d.keys())
    for i, (k, v) in enumerate(d.items()):
        connector = "└── " if i == len(keys) - 1 else "├── "
        print(pad + Fore.GREEN + connector + Fore.WHITE + k + Style.RESET_ALL)
        if isinstance(v, dict):
            extension = "    " if i == len(keys) - 1 else "│   "
            tree(v, pad + extension)