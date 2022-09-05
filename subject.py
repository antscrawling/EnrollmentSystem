import os
import json
import pandas as pd
import PySimpleGUI as sg
from pandas.io.json._normalize import nested_to_record  
def loadfile(subdict):
    thisdict ={}
    if os.path.exists('subjects.json'):

        with open('subjects.json','r') as a1:
            thisdict = json.load(a1)

        print('loaded the {} file'.format(a1))
        a1.close()
        return thisdict
    else:
        x1 = open('subjects.json','w')
        json.dump(subdict,x1)
        return subdict

def savefile(subdict):
    with open('subjects.json','w') as a2:
        json.dump(subdict,a2)
        a2.close()
    
        


def addsubjects(subdict):
    addlayout = [
            [sg.Text('Add Subjects Maintenance',justification='center', text_color='Blue',size = 50)],
            [sg.Text('Subject ID     ',justification='left', text_color='Blue',size = 20),sg.Input(key='subid')],
            [sg.Text('Subject Name   ',justification='left', text_color='Blue',size = 20),sg.Input(key='subname')],
            [sg.Text('Subject Teacher',justification='left', text_color='Blue',size = 20),sg.Input(key='teacher')],
            [sg.Text('Subject Term   ',justification='left', text_color='Blue',size = 20),sg.Input(key='term')],
            [sg.Text('Subject Units  ',justification='left', text_color='Blue',size = 20),sg.Input(key='units')],
            [sg.Text('',key='addtext',justification='left',text_color='Blue',size = 20)],
            [sg.Submit(),sg.Cancel()]
    ]
    wind7 = sg.Window('Adding New Subjects',addlayout)

    while True:
        event,value = wind7.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            wind7.close()
            break
        elif event == 'Submit':
            wind7['addtext'].update('Adding Subject ID {}'.format(value['subid']) )            
            newdict ={}
            newdict = {value['subid']:{'subname':value['subname'],
            'teacher':value['teacher'],
            'term':value['term'],
            'units':value['units']}
                        }
            subdict.update(newdict)
            savefile(subdict)     
            wind7.close()     


def editsubjects(subdict):
    editlayout = [
            [sg.Text(size=50)],
            [sg.OptionMenu(subdict.keys(),size=20),
            sg.Submit(),sg.Cancel()],
            [sg.Text(size=50)]
    ]
    wind3 = sg.Window('Editing Existing Subjects',editlayout)
    while True:
        
        event,values = wind3.read()
        subid = values[0]
        if event == sg.WIN_CLOSED or event == 'Cancel':
            wind3.close()
            break
        elif event == 'Submit':
            valuelayout = [
            [sg.Text('Subject ID : ',size=20),sg.Text(subid,key='subid',size=35)],
            [sg.Text('Subject Name',size=20),sg.Input(subdict[subid]['subname'],key='subname',size=20)],
            [sg.Text('Subject Teacher',size=20),sg.Input(subdict[subid]['teacher'],key='teacher',size=20)],
            [sg.Text('Subject Term',size=20),sg.Input(subdict[subid]['term'],key='term',size=20)],
            [sg.Text('Subject Units',size=20),sg.Input(subdict[subid]['units'],key='units',size=20)],
            [sg.Submit(),sg.Cancel()],
            [sg.Text(size=50)]
                ]
            wind4 = sg.Window('Editing Existing Subjects',valuelayout)
            while True:
                event2, value2 = wind4.read()
                if event2 == sg.WINDOW_CLOSED or event2 == 'Cancel':
                    wind4.close()
                    break
                elif event2 == 'Submit':
                    subdict[subid]['subname'] = value2['subname']
                    subdict[subid]['teacher'] = value2['teacher']
                    subdict[subid]['term'] = value2['term']
                    subdict[subid]['units'] = value2['units']
                    savefile(subdict)
                    df = pd.DataFrame.from_dict(subdict)
                    print(df)
                    wind4.close()
                    break
            wind4.close()
            continue
    wind3.close()
def showdelrec(subid,subdict):
    showlayout = [ 
        [sg.Text('Subject ID       ',size=20),sg.Text(subid,justification='left', text_color='Blue',size = 20)],
        [sg.Text('Subject Name     ',size=20),sg.Text(subdict[subid]['subname'],justification='left', text_color='Blue',size = 20)],
        [sg.Text('Subject Teacher  ',size=20),sg.Text(subdict[subid]['teacher'],justification='left', text_color='Blue',size = 20)],
        [sg.Text('Subject Term     ',size=20),sg.Text(subdict[subid]['term'],justification='left', text_color='Blue',size = 20)],
        [sg.Text('Subject Units    ',size=20),sg.Text(subdict[subid]['units'],justification='left', text_color='Blue',size = 20)],
        [sg.Text('Delete This Record?')],
        [sg.Submit(),sg.Cancel()]

    ]
    showwind = sg.Window('Record to be Deleted',showlayout)      
    while True:
        events, value = showwind.read()
        if events == sg.WIN_CLOSED:
            showwind.close()
            break
        elif events == 'Cancel':
            showwind.close()
            break
        elif events == 'Submit':
            subdict.pop(subid)
            print(subdict)
            showwind.close()
            break

def deletesubjects(subdict):
    deletelayout = [
            [sg.Text(size=50)],
            [sg.OptionMenu(subdict.keys(),size=20,key='subid'),
            sg.Submit(),sg.Cancel()],
            [sg.Text(size=50)]
    ]
    wind3 = sg.Window('Deleting Existing Subjects',deletelayout)
    while True:
        
        event,values = wind3.read()
        subid = values['subid']
        if event == sg.WIN_CLOSED or event == 'Cancel':
            wind3.close()
            break
        elif event == 'Submit':
            showdelrec(subid,subdict)
            wind3.close()
            break


def submain():
    subdict = {}
    subdict = {None:None}
    enrolldict = {}
    if not os.path.exists('subjects.json'):
        a4 = open('subjects.json','w')
        json.dump(subdict,a4)
        a4.close()
    else :
        subdict = loadfile(subdict)
    sg.theme('Purple')
    layout = [  
            [sg.Text('Subjects Maintenance',justification='center', text_color='Blue',size = 30)],
            [sg.Button('Add    Subjects',size=14,key='Add'),sg.Text('Add new records',justification='left',size=30)],
            [sg.Button('Edit   Subjects',size=14,key='Edit'),sg.Text('Edit Existing records',justification='left',size=30)],
            [sg.Button('Delete Subjects',size=14,key='Delete'),sg.Text('Delete Existing records',justification='left',size=30)],
            [sg.Button('View Subjects',size=14,key='View'),sg.Text('View Existing records',justification='left',size=30)],
            [sg.Cancel(size=14),sg.Text('Cancel  ',justification='left', size=30)]
        ]
    wind2 = sg.Window('Subjects Maintenance Program',layout)

    while True:
        event,value = wind2.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            wind2.close()
            break
        elif event == 'Add':
            addsubjects(subdict)
            continue
        elif event == 'Edit':
            editsubjects(subdict)
            continue
        elif event == 'Delete':
            deletesubjects(subdict)
            continue
        elif event == 'View':
            flat = nested_to_record(subdict, sep='_')
            #df = pd.DataFrame.from_dict(studdict)
            sg.Popup(flat)
            continue


if __name__ == '__main__':
    submain()


