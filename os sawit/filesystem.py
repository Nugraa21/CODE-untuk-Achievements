import json

FS_PATH = "storage/fs.json"

def load_fs():
    with open(FS_PATH, "r") as f:
        return json.load(f)

def save_fs(fs):
    with open(FS_PATH, "w") as f:
        json.dump(fs, f, indent=2)

def get_dir(fs, path):
    cur = fs["/"]
    for p in [x for x in path.split("/") if x]:
        cur = cur[p]
    return cur
