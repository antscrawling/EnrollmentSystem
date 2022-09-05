
import stud
import subject
import enroll
import PySimpleGUI as sg


def main():
    sg.theme('Dark Blue 3')
    layout = [  [sg.Text(size=40)],
            [sg.Text('Enrollment Program',justification='center', text_color='Orange',border_width=1,size = (70,1))],
            [sg.Text(size=40)],
            [sg.Button('Students',size=(40,1)),sg.Text('Students Maintenance ',text_color='Orange',justification='left', size=(40,1))],
            [sg.Button('Subjects',size=(40,1)),sg.Text('Subjects Maintenance ',text_color='Orange',justification='left', size=(40,1))],
            [sg.Button('Enrollment',size=(40,1)),sg.Text('Enrollment Registration  ',text_color='Orange',justification='left', size=(40,1))],
            [sg.Button('Cancel',size=(40,1)),sg.Text('Cancel  ',text_color='Orange',justification='left', size=(40,1))],
            [sg.Text(size=40)]
        ]
    wind1 = sg.Window('University System', layout,
    default_element_size=(40, 1), grab_anywhere=False)
    while True:
        event, values = wind1.read()
        if event == 'Students':


            stud.studmain()
            continue
        elif event == 'Subjects':

            subject.submain()
            continue
        elif event == 'Enrollment':

            enroll.enrollmain()
            continue
        elif event == sg.WINDOW_CLOSED or event == 'Cancel' :
            break
    wind1.close()    

if __name__ == '__main__':
    main()



