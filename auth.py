import PySimpleGUI as sg
import json
import os
from user_manager import UserManager

user_manager = UserManager()

def load_data():
    """ Load existing data from the JSON file """
    if not os.path.exists("users.json"):
        with open("users.json", "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    """ Save data to the JSON file """
    with open("users.json", "w") as f:
        json.dump(data, f)


def register_user(username, password):
    """ Register a new user """
    data = load_data()
    if username in data:
        return False  #user already exists
    data[username] = password
    save_data(data)
    return True

def register(username, password):
    data = load_data()
    if username in data:
        return False, "User exists"
    data[username] = password
    save_data(data)
    return True, "User registered"

def login(username, password):
    data = load_data()
    if data.get(username) == password:
        user_manager.current_user = username
        user_manager.current_pass = password
        user_manager.current_status = "logged in"
        return True, "User logged in"
    return False, "Invalid credentials"

def create_login():
    """ Create the login form """
    layout = [
        [sg.Text("Username:"), sg.InputText(key="username")],
        [sg.Text("Password:"), sg.InputText(key="password", password_char="*")],
        [sg.Button("Login"), sg.Button("Register")]
    ]

    window = sg.Window("Authentication", layout, finalize = True)


    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Exit"):
            break
        username = values[username]
        password = values[password]

        if event == "Login":
            if not username or not password:
                window["error"].update("Please enter both username and password")
                continue
            login_status = user_manager.login(username, password)
            if login_status == "Login Success":
                sg.popup("Login successful")
                break
            else: 
                window["error"].update("Invalid credentials")

        elif event == "Register":
            if not username or not password:
                window["error"].update("Please enter both username and password")
                continue
            register_status = user_manager.register(username, password)
            if register_status == "Registration Success":
                sg.popup("Registration successful")
                break
            else:
                window["error"].update("User already exists")

    window.close()

if __name__ == "__main__":
    create_login()

            


