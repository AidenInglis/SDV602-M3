import PySimpleGUI as sg#importing pysimplegui as sg




def create_screen1():#declaring the function for creating screen 1

    left_col = [#making the left column for the chart placeholder
        [sg.Canvas(size=(200, 200), background_color='white', key='chart1_placeholder')],#canvas = chart placeholder
        [sg.Button('Back to Lobby')]#back to Lobby button
    ]

    right_col = [#making the right column for the chat system and buttons
        [sg.Multiline(size=(30, 10), key='screen1_chat', disabled=True)],#chat history
        [sg.Input(key='screen1_chat_input')], [sg.Button('Send Chat 1'), sg.Button("Zoom In"), sg.Button("Zoom Out")]#chat-input and send-button
    ]

    summary_col = [#summary info box
        [sg.Text('Fields:', size=(20, 1))],#sumary title
        [sg.Text('Field 1:', size=(8, 1))],#label for field 1
        [sg.Text('', key='screen1_field1')],#empty field for field 1
        [sg.Text('Field 2:', size=(8, 1))],#label for field 2
        [sg.Text('', key='screen1_field2')],#empty field for field 2
    ]

    screen = [#declaring the layout of the screen
        [sg.Text('Screen 1')],#title of the screen
        [sg.Column(left_col, vertical_alignment='top', element_justification='center', pad=(10, 10)),#left col
        sg.Column(right_col, vertical_alignment='top', element_justification='center', pad=(10, 10)),#right col
        sg.Frame('Summary Info', summary_col, element_justification='left', pad=(10, 10))]#summary info box on the left side but third col.
    ]
    return screen#return the screen


def create_screen2():#declaring the function for creating screen 2
    left_col = [#making the left column for the chart placeholder
        [sg.Canvas(size=(200, 200), background_color='white', key='chart2_placeholder')],#canvas = chart placeholder
        [sg.Button('Back to Lobby')]#back to Lobby button
    ]

    right_col = [#making the right column for the chat system and buttons
        [sg.Multiline(size=(30, 10), key='screen2_chat', disabled=True)],#chat history
        [sg.Input(key='screen2_chat_input')], [sg.Button('Send Chat 2'), sg.Button("Zoom In"), sg.Button("Zoom Out")]#chat-input and send-button
    ]

    summary_col = [#summary info box
        [sg.Text('Fields:', size=(20, 1))],#sumary title
        [sg.Text('Field 1:', size=(8, 1))],#label for field 1
        [sg.Text('', key='screen2_field1')],#empty field for field 1
        [sg.Text('Field 2:', size=(8, 1))],#label for field 2
        [sg.Text('', key='screen2_field2')],#empty field for field 2
    ]

    screen = [#declaring the layout of the screen
        [sg.Text('Screen 2')],#title of the screen
        [sg.Column(left_col, vertical_alignment='top', element_justification='center', pad=(10, 10)),#left col
        sg.Column(right_col, vertical_alignment='top', element_justification='center', pad=(10, 10)),#right col
        sg.Frame('Summary Info', summary_col, element_justification='left', pad=(10, 10))]#summary info box on the left side but third col.
    ]
    return screen#return the screen

def create_screen3():#declaring the function for creating screen 3
    left_col = [#making the left column for the chart placeholder
        [sg.Canvas(size=(200, 200), background_color='white', key='chart3_placeholder')],#canvas = chart placeholder
        [sg.Button('Back to Lobby')]#back to Lobby button
    ]

    right_col = [#making the right column for the chat system and buttons
        [sg.Multiline(size=(30, 10), key='screen3_chat', disabled=True)],#chat history
        [sg.Input(key='screen3_chat_input')], [sg.Button('Send Chat 3'), sg.Button("Zoom In"), sg.Button("Zoom Out")]#chat-input and send-button
    ]

    summary_col = [#summary info box
        [sg.Text('Fields:', size=(20, 1))],#sumary title
        [sg.Text('Field 1:', size=(8, 1))],#label for field 1
        [sg.Text('', key='screen3_field1')],#empty field for field 1
        [sg.Text('Field 2:', size=(8, 1))],#label for field 2
        [sg.Text('', key='screen3_field2')],#empty field for field 2
    ]

    screen = [#declaring the layout of the screen
        [sg.Text('Screen 3')],#title of the screen
        [sg.Column(left_col, vertical_alignment='top', element_justification='center', pad=(10, 10)),#left col
        sg.Column(right_col, vertical_alignment='top', element_justification='center', pad=(10, 10)),#right col
        sg.Frame('Summary Info', summary_col, element_justification='left', pad=(10, 10))]#summary info box on the left side but third col.
    ]
    return screen#return the screen

def create_login():#testing the login screen, not active right now as it was taken from todd's code
    """ Login screen """
    layout = [
        [sg.Text('Login')],
        [sg.Text('Username'), sg.InputText(key='username')],
        [sg.Text('Password'), sg.InputText(key='password', password_char='*')],
        [sg.Button('Login'), sg.Button('Back')]
    ]
    return layout

def create_register():#testing the register screen, not active right now as it was taken from todd's code
    """ Registration screen """
    layout = [
        [sg.Text('Register')],
        [sg.Text('Username'), sg.InputText(key='username')],
        [sg.Text('Password'), sg.InputText(key='password', password_char='*')],
        [sg.Text('Confirm Password'), sg.InputText(key='confirm_password', password_char='*')],
        [sg.Button('Register'), sg.Button('Back')]
    ]
    return layout