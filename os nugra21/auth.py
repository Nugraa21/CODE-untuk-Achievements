from storage import load, save

USER_DB = "data/users.json"

def login():
    users = load(USER_DB, {
        "nugra": {"password": "123", "home": "/home/nugra"}
    })

    print("Login to Nugra21OS")
    while True:
        user = input("username: ")
        pwd = input("password: ")

        if user in users and users[user]["password"] == pwd:
            print("Login successful\n")
            return user, users[user]["home"]
        else:
            print("Login incorrect\n")
