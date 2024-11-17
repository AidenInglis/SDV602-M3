from screens import create_lobby, create_login, create_register, create_screen1, create_screen2, create_screen3, create_default_screen
from user_manager import register_user, authenticate_user
from chart import draw_chart, zoom_in, zoom_out
import PySimpleGUI as sg
import sys
sys.dont_write_bytecode = True
#from auth import LoginView
#from chat_view import ChatView


def main():
    window = sg.Window('Data Analyst Program', create_lobby(), finalize=True)
    chat_logs = {'screen1': [], 'screen2': [], 'screen3': []}

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Login':
            window.close()
            window = sg.Window('Login', create_login(), finalize=True)
        elif event == 'Register':
            window.close()
            window = sg.Window('Register', create_register(), finalize=True)
        elif event == 'Back':
            window.close()
            window = sg.Window('Chart Application', create_lobby())
        elif event == "Zoom In":
            zoom_in()  #zoom in on the current chart
        elif event == "Zoom Out":
            zoom_out()
        #handle login form submission
        elif event == 'Login' and values['username'] and values['password']:
            if authenticate_user(values['username'], values['password']):
                window.close()
                window = sg.Window('Chart Application', create_lobby(),finalize=True)
            else:
                sg.popup_error('Invalid credentials')

        #handle registration form submission
        elif event == 'Register' and values['username'] and values['password'] == values['confirm_password']:
            if register_user(values['username'], values['password']):
                sg.popup('Registration successful! Please log in.')
                window.close()
                window = sg.Window('Login', create_login(), finalize=True)
            else:
                sg.popup_error('User already exists or registration failed')

        elif event == 'Screen 1':
            window.close()
            window = sg.Window('Screen 1', create_screen1(), finalize=True)
            draw_chart(window['chart1_placeholder'])
        elif event == 'Screen 2':
            window.close()
            window = sg.Window('Screen 2', create_screen2(), finalize=True)
            draw_chart(window['chart2_placeholder'])
        elif event == 'Screen 3':
            window.close()
            window = sg.Window('Screen 3', create_screen3(), finalize=True)
            draw_chart(window['chart3_placeholder'])
        elif event == 'Back to Lobby':
            window.close()
            window = sg.Window('Chart Application', create_lobby())
        elif event == 'ByPass Lobby':
            window.close()
            window = sg.Window('Chart Application', create_default_screen(), finalize=True)

    window.close()

if __name__ == "__main__":
    main()
