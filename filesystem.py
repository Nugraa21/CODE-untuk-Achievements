# Fake filesystem (RAM only)

filesystem = {
    "/": {
        "home": {
            "nugra": {
                "readme.txt": "Welcome to Nugra21OS\nThis is a fake terminal OS.",
                "todo.txt": "- Learn Python\n- Build fake OS\n- Push to GitHub"
            }
        },
        "etc": {
            "os-release": "Nugra21OS v1.0"
        }
    }
}

current_path = ["/", "home", "nugra"]

def get_dir():
    d = filesystem["/"]
    for p in current_path[1:]:
        d = d[p]
    return d

def pwd():
    return "/".join(current_path).replace("//", "/")
