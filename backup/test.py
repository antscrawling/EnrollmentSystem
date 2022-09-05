import PySimpleGUI as sg

sg.theme('Purple')
layout = [  
            [sg.Text('TExt',key='output',size=20)],
            [sg.Button('Submit',size=10),sg.Button('Cancel',size=10)]

        ]
wind = sg.Window('This is the new Window',layout)
while True:
    events,value = wind.read()
    if events == sg.WINDOW_CLOSED or events == 'Cancel':
        break
    elif events == 'Submit':
        pass

