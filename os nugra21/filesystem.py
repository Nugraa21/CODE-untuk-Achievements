import json
import os

FS_PATH = "storage/fs.json"

DEFAULT_FS = {
    "/": {
        "home": {
            "nugra": {
                "readme.txt": "Welcome to Nugra21OS\nThis is a fake terminal OS.",
                "todo.txt": "- Learn Python\n- Build fake OS\n- Push to GitHub"
            }
        },
        "etc": {},
        "var": {},
        "tmp": {}
    }
}

# load or repair filesystem
def load_fs():
    if not os.path.exists(FS_PATH):
        save_fs(DEFAULT_FS)
        return DEFAULT_FS

    try:
        with open(FS_PATH, "r") as f:
            fs = json.load(f)
            if "/" not in fs:
                raise ValueError
            return fs
    except:
        save_fs(DEFAULT_FS)
        return DEFAULT_FS

def save_fs(fs):
    os.makedirs("storage", exist_ok=True)
    with open(FS_PATH, "w") as f:
        json.dump(fs, f, indent=2)

fs = load_fs()
cwd = ["/"]

def pwd():
    return "/".join(cwd).replace("//", "/")

def get_dir():
    d = fs["/"]
    for p in cwd[1:]:
        d = d[p]
    return d

def cd(path):
    global cwd
    if path == "/":
        cwd = ["/"]
        return True
    if path == "..":
        if len(cwd) > 1:
            cwd.pop()
        return True
    d = get_dir()
    if path in d and isinstance(d[path], dict):
        cwd.append(path)
        return True
    return False
