import PySimpleGUI as sg#sample window that i created for after the user logs in


def create_lobby():#declaring the function for creating the default screen
    screen = [
        [sg.Text('Please login to access the application.')],#login message
        [sg.Button('Screen 1'), sg.Button('Screen 2'), sg.Button('Screen 3'), sg.Button('Exit')]#chart buttons
    ]

    lobby_window = sg.Window('Chart Application', screen, finalize=True)#creating the window
    return screen
