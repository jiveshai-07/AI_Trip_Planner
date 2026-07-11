import json
import hashlib
import os

USERS_FILE = "data/users.json"


def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def save_users(users):
    os.makedirs("data", exist_ok=True)
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)


def hash_password(password):
    salt = "trip_planner_salt_2026"
    return hashlib.sha256((password + salt).encode()).hexdigest()


def username_exists(username):
    users = load_users()
    return username.lower() in users


def register_user(username, password, email=""):
    users = load_users()
    username_key = username.lower()

    if username_key in users:
        return False, "Username already exists."

    users[username_key] = {
        "username": username,
        "password_hash": hash_password(password),
        "email": email
    }

    save_users(users)
    return True, "Account created successfully."


def verify_user(username, password):
    users = load_users()
    username_key = username.lower()

    if username_key not in users:
        return False

    stored_hash = users[username_key]["password_hash"]
    return stored_hash == hash_password(password)