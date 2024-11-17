from screens import create_login, create_register, create_screen1, create_screen2, create_screen3
from chart import draw_chart, zoom_in, zoom_out
import PySimpleGUI as sg
import sys
from services import Services
from lobby import create_lobby 
from user_manager import UserManager
from auth import create_login


def main():
    user_manager = UserManager()

    service = Services(file_path='data.json')
    create_login()

    if user_manager.current_status == "Logged In":
        current_window = create_lobby()
    

        while True:
            event, values = current_window.read()

            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            elif event == 'Back':
                current_window.close()
                current_window = sg.Window('Chart Application', create_lobby())
            elif event == "Zoom In":
                zoom_in()  #zoom in on the current chart
            elif event == "Zoom Out":
                zoom_out()#zoom out on the current chart
            elif event == 'Screen 1':
                current_window.close()
                current_window = sg.Window('Screen 1', create_screen1(), finalize=True)
                draw_chart(current_window['chart1_placeholder'])
            elif event == 'Screen 2':
                current_window.close()
                current_window = sg.Window('Screen 2', create_screen2(), finalize=True)
                draw_chart(current_window['chart2_placeholder'])
            elif event == 'Screen 3':
                current_window.close()
                current_window = sg.Window('Screen 3', create_screen3(), finalize=True)
                draw_chart(current_window['chart3_placeholder'])
            elif event == 'Back to Lobby':
                current_window.close()
                current_window = sg.Window('Chart Application', create_lobby())
            elif event == 'ByPass Lobby':
                current_window.close()
                current_window = sg.Window('Chart Application', create_lobby(), finalize=True)

        current_window.close()

if __name__ == "__main__":
    main()
