import json
import os

def load(path, default):
    if not os.path.exists(path):
        save(path, default)
    with open(path, "r") as f:
        return json.load(f)

def save(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
