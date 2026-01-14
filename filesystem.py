import json

PATH = "storage/fs.json"

def load_fs():
    with open(PATH, "r") as f:
        return json.load(f)

def save_fs(fs):
    with open(PATH, "w") as f:
        json.dump(fs, f, indent=2)

def get_dir(fs, cwd):
    cur = fs["/"]
    for p in [x for x in cwd.split("/") if x]:
        cur = cur[p]
    return cur
