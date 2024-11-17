from json_drop_service import JsnDrop
import json
import os

#check users file exists, if not then create
USER_FILE = "users.json"

def load_users():
    """ Load existing users from the JSON file """
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    """ Save users to the JSON file """
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

def register_user(username, password):
    """ Register a new user """
    users = load_users()
    if username in users:
        return False  #user already exists
    users[username] = password
    save_users(users)
    return True

def authenticate_user(username, password):
    """ Authenticate the user for login """
    users = load_users()
    if users.get(username) == password:
        return True
    return False
