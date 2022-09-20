#!/usr/local/bin/python
import stud
import subject
import enroll
import PySimpleGUI as sg


def mainmenu():
    sg.theme('Purple')
    layout = [  [sg.Text(size=40)],
            [sg.Text('Enrollment Program',font = ('Arial',20),justification='center', text_color='Blue',border_width=1,size = (30,1))],
            [sg.Text(size=40)],
            [sg.Button('Students',font = ('Arial',20),size=(20,1)),sg.Text('Students Maintenance ',font = ('Arial',20),text_color='Blue',justification='left', size=(20,1))],
            [sg.Button('Subjects',font = ('Arial',20),size=(20,1)),sg.Text('Subjects Maintenance ',font = ('Arial',20),text_color='Blue',justification='left', size=(20,1))],
            [sg.Button('Enrollment',font = ('Arial',20),size=(20,1)),sg.Text('Enrollment Registration  ',font = ('Arial',20),text_color='Blue',justification='left', size=(20,1))],
            [sg.Button('Cancel',font = ('Arial',20),size=(20,1)),sg.Text('Cancel',text_color='Blue',justification='left',font = ('Arial',20), size=(20,1))],
            [sg.Text(size=40)]
        ]
    wind1 = sg.Window('University System', layout)
  
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

#if __name__ == '__main__':
#    main()


