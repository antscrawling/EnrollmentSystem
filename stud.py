
import os
import json
import pandas as pd
import PySimpleGUI as sg
from pandas.io.json._normalize import nested_to_record  

def loadfile(studdict):
    #studdict = {'studid':[],'fname':[],'mname':[],'lname':[],'rate':[]}
    with open('students.json','r') as f1:
        studdict = json.load(f1)
        print('loaded the {} file'.format(f1))
        f1.close()
    return studdict

def savefile(studdict):
    with open('students.json','w') as f2:
        json.dump(studdict,f2)
        f2.close()
    return studdict
        


def addstudents(studdict):
    addlayout = [
            [sg.Text('Add Students Maintenance',justification='center', text_color='Blue',size = 50)],
            [sg.Text('Student ID ',justification='left', text_color='Blue',size = (20,1)),sg.Input(key='studid')],
            [sg.Text('Student First Name',justification='left', text_color='Blue',size = (20,1)),sg.Input(key='fname')],
            [sg.Text('Student Middle Name',justification='left', text_color='Blue',size = (20,1)),sg.Input(key='mname')],
            [sg.Text('Student Last Name',justification='left', text_color='Blue',size = (20,1)),sg.Input(key='lname')],
            [sg.Text('Student Rate',justification='left', text_color='Blue',size = (20,1)),sg.Input(key='rate')],
            [sg.Text('',key='addtext',justification='left',text_color='Blue',size = (20,1))],
            [sg.Submit(),sg.Cancel()]
    ]
    wind7 = sg.Window('Adding New Students',addlayout)

    while True:
        event,value = wind7.read()

    #load the existing dict
    #studdict = loadfile('students.json',studdict)
    #newstuddict[studid]={'fname':fname,'mname':mname,'lname':lname,'rate':rate}
    #studdict.update(newstuddict)
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            wind7.close()
            break
        elif event == 'Submit':
            wind7['addtext'].update('Adding Student ID {}'.format(value['studid']) )            
            newdict ={}
            newdict = {value['studid']:{'fname':value['fname'],
            'mname':value['mname'],
            'lname':value['lname'],
            'rate':value['rate']}
                        }
            studdict.update(newdict)
            savefile(studdict)     
            wind7.close()     
             
            break



    



def editstudents(studdict):
    editlayout = [
            [sg.Text(size=50)],
            [sg.OptionMenu(studdict.keys(),size = (20,1)),
            sg.Submit(),sg.Cancel()],
            [sg.Text(size=50)]
    ]
    wind3 = sg.Window('Editing Existing Students',editlayout)

    while True:
        event1,value1 = wind3.read()

    #load the existing dict
    #studdict = loadfile('students.json',studdict)
    #newstuddict[studid]={'fname':fname,'mname':mname,'lname':lname,'rate':rate}
    #studdict.update(newstuddict)
        if event1 == sg.WINDOW_CLOSED or event1 == 'Cancel':
            wind3.close()
            break
        elif event1 == 'Submit':
            studid = value1[0]
            valuelayout = [
            [sg.Text('Student ID : ',size = (20,1)),sg.Text(studid,size=35)],
            [sg.Text('Student First Name',size = (20,1)),sg.Input(studdict[studid]['fname'],key='fname',size = (20,1))],
            [sg.Text('Student Middle Name',size = (20,1)),sg.Input(studdict[studid]['mname'],key='mname',size = (20,1))],
            [sg.Text('Student Last Name',size = (20,1)),sg.Input(studdict[studid]['lname'],key='lname',size = (20,1))],
            [sg.Text('Student Units',size = (20,1)),sg.Input(studdict[studid]['rate'],key='rate',size = (20,1))],
            [sg.Submit(),sg.Cancel()],
            [sg.Text(size=50)]
                ]
            wind4 = sg.Window('Editing Existing Students',valuelayout)
            while True:
                event2, value2 = wind4.read()
                if event2 == sg.WINDOW_CLOSED or event2 == 'Cancel':
                    wind4.close()
                    break
                elif event2 == 'Submit':
                    studdict[studid]['fname'] = value2['fname']
                    studdict[studid]['mname'] = value2['mname']
                    studdict[studid]['lname'] = value2['lname']
                    studdict[studid]['rate'] = value2['rate']
                    savefile(studdict)
                    df = pd.DataFrame.from_dict(studdict)
                    print(df)
                    wind4.close()
                    break
            wind4.close()
            continue
    wind3.close()
           
def showdelrec(studid,studdict):
    showlayout = [ 
        [sg.Text('Student ID    ',size = (20,1)),sg.Text(studid,justification='left', text_color='Blue',size = (20,1))],
        [sg.Text('Student Name  ',size = (20,1)),sg.Text(studdict[studid]['fname'],justification='left', text_color='Blue',size = (20,1))],
        [sg.Text('Student Middle',size = (20,1)),sg.Text(studdict[studid]['mname'],justification='left', text_color='Blue',size = (20,1))],
        [sg.Text('Student Last  ',size = (20,1)),sg.Text(studdict[studid]['lname'],justification='left', text_color='Blue',size = (20,1))],
        [sg.Text('Student Rate  ',size = (20,1)),sg.Text(studdict[studid]['rate'],justification='left', text_color='Blue',size = (20,1))],
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
            studdict.pop(studid)
            print(studdict)
            showwind.close()
            break
    

def deletestudents(studdict):
    
    deletelayout = [
            [sg.Text(size=50)],
            [sg.OptionMenu(studdict.keys(),size = (20,1),key='studid'),
            sg.Submit(),sg.Cancel()],
            [sg.Text(size=50)]
            ]
    winddel = sg.Window('Deleting Existing Students',deletelayout)

    while True:
        event,value = winddel.read()
        if event == sg.WIN_CLOSED:
            winddel.close()
            break
        if event == 'Cancel':
            winddel.close()
            break
        if event == 'Submit':
            showdelrec(value['studid'],studdict)
            winddel.close()
            break



def studmain():
    studdict = {None:None}
    subdict = {}
    enrolldict = {}
    if not os.path.exists('students.json'):
        fx = open('students.json','w')
        json.dump(studdict,fx)
        studdict = loadfile(studdict)
        fx.close()
    else :
        studdict = loadfile(studdict)
    sg.theme('Purple')
    layout = [  
            [sg.Text('Students Maintenance',justification='center', text_color='Blue',size = (20,1))],
            [sg.Button('Add    Students',size = (20,1),key='Add'),sg.Text('Add new records',justification='left',size = (20,1))],
            [sg.Button('Edit   Students',size = (20,1),key='Edit'),sg.Text('Edit Existing records',justification='left',size = (20,1))],
            [sg.Button('Delete Students',size = (20,1),key='Delete'),sg.Text('Delete Existing records',justification='left',size = (20,1))],
            [sg.Button('View Students',size = (20,1),key='View'),sg.Text('View Existing records',justification='left',size = (20,1))],
            [sg.Cancel(size = (20,1)),sg.Text('Cancel',justification='left', size = (20,1))],
        ]
    wind2 = sg.Window('University System', layout)
    
    while True:
        event, values = wind2.read()
        if event == 'Add':
            addstudents(studdict)
            continue

        elif event == 'Edit':
            editstudents(studdict)
            continue

        elif event == 'Delete':
            print('delete')
            deletestudents(studdict)
            continue
        elif event == 'View':
            flat = nested_to_record(studdict, sep='_')
            #df = pd.DataFrame.from_dict(studdict)
            sg.Popup(flat)
            continue
        elif event == sg.WINDOW_CLOSED or event == 'Cancel' :
            wind2.close()
            break
    


if __name__ == '__main__':
    studmain()
    

