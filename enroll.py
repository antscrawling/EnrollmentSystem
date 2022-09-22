import json
import PySimpleGUI as sg
import pandas as pd

def loadfile(enrolldict):
    with open('enroll.json','r') as f1:
        enrolldict = json.load(f1)
        print('loaded the {} file'.format(f1))
        f1.close()
    return enrolldict
def savefile(enrolldict):
    with open('enroll.json','w') as f2:
        json.dump(enrolldict,f2)
        f2.close()
    return enrolldict

def print_tuition(enrolldict):
    term = 'TERM012022'
    #stud = input('Student: ')
    

    enrolldict = loadfile(enrolldict)
    #print(enrolldict[stud+term]['amount'])
    newlist = []
    newdict = {}
    x = 0
    for k,v in enrolldict.items():
        if v['term'] == term:
            newlist.append(v['studid'])
            newlist.append(v['subid'])
            newlist.append(v['term'])
            newlist.append(v['amount'])
    print(len(newlist))
    twolist = []
    threelist =[]
    newdict = {}
    amount = 0 
    onelist = [x for x in range(0,len(newlist),4)]
    for y in onelist:     
        # 0  term, 1 student 2 subject 3 amount   
        #print("TERM {}, stud {}, sub {} amount {}".format(newlist[y+2],newlist[y],newlist[y+1],newlist[y+3]))
        twolist.append(newlist[y])
        twolist.append(newlist[y+3])
    #print(twolist)

    for x in range(0,len(twolist),2):
        stud = twolist[x]
        if stud in newdict.keys():
            amount  = twolist[x+1] + newdict[stud]
            newdict[stud] = amount
            newdict.update(newdict)
        else:
            amount = twolist[x+1]
            newdict[stud] = amount
            newdict.update(newdict)
        #print(stud,amount)
        
    sg.Popup(newdict,font=('Arial',20))







    print(newdict)

    

#        if not y+6 > len(newlist):
#            term2 = newlist[y+6]
#            stud2 = newlist[y+4]
#            amount2 = newlist[y+7]
#            if  term1+stud1 == term2+stud2:
#                amount1 += amount2
#                newdict[term1+stud1] = amount1
#            else:
#                newdict[term2+stud2] = amount2
#        
        
    print(newdict)



    # term, student, amount

    #print(threelist)
    

    
    

        



def addenrollment(enrolldict,studdict,subdict):
    newdict ={}
    sg.theme('Purple')
    addlayout = [
            [sg.Text('',size=20)],
            [sg.Text('Student ID',size=10,font=('Arial',20)),sg.OptionMenu(studdict.keys(),size=20,key='studid'),
             sg.Text('',size=20)],
            [sg.Text('Subject ID',size=10,font=('Arial',20)),sg.OptionMenu(subdict.keys(),size=20,key='subid'),
             sg.Text('',size=20)],
            [sg.Text('Term',size=10,font=('Arial',20)),sg.OptionMenu(('TERM012022','TERM022022','TERM032022'),size=20,key='term')
             ,sg.Submit()],
            [sg.Text('',size=50)],
            [sg.Text('Subject Name',size = (20,1),font=('Arial',20)),sg.Text('',key='subname',size = (20,1),text_color='Blue',font=('Arial',20))],
            [sg.Text('Teacher Name',size = (20,1),font=('Arial',20)),sg.Text('',key='teacher',size = (20,1),text_color='Blue',font=('Arial',20))],
            [sg.Text('Units',size = (20,1),font=('Arial',20)),sg.Text('',key='units',size = (20,1),text_color='Blue',font=('Arial',20))],
            [sg.Text('Amount',size = (20,1),font=('Arial',20)),sg.Text('',key='amount',size = (20,1),text_color='Blue',font=('Arial',20))],
            [sg.Text('First Name',size = (20,1),font=('Arial',20)),sg.Text('',key='fname',size = (20,1),text_color='Blue',font=('Arial',20))],
            [sg.Text('Middle Name',size = (20,1),font=('Arial',20)),sg.Text('',key='mname',size = (20,1),text_color='Blue',font=('Arial',20))],
            [sg.Text('Last Name',size = (20,1),font=('Arial',20)),sg.Text('',key='lname',size = (20,1),text_color='Blue',font=('Arial',20))],  
            [sg.Text('',key='message',size=50,font=('Arial',20))],         
            [sg.Cancel(font=('Arial',20)),sg.Button('ENROLL',font=('Arial',20))]            
            ]
    wind = sg.Window('Enrollment Registration',addlayout)   
    while True:
        event, values = wind.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            wind.close()
            break  
        elif event == 'Submit':
            #get the values from the tables
            studid = values['studid']
            subid = values['subid']
            term = values['term']
            teacher = subdict[subid]['teacher']
            units = subdict[values['subid']]['units']
            fname = studdict[values['studid']]['fname']
            mname = studdict[values['studid']]['mname']
            lname = studdict[values['studid']]['lname']
            #compute the amount of enrollment
            amount = (float(subdict[values['subid']]['units']) * float(studdict[values['studid']]['rate'])).__round__(2)
            #update the window with the information
            wind['teacher'].update(teacher)
            wind['units'].update(units)
            wind['amount'].update(amount)
            wind['fname'].update(fname)
            wind['mname'].update(mname)
            wind['lname'].update(lname)
            #save the info to dictionary
        elif event == 'ENROLL':
            olddict ={}
            olddict = loadfile(enrolldict)
            studid = values['studid']
            subid = values['subid']
            term = values['term']
            teacher = subdict[subid]['teacher']
            units = subdict[values['subid']]['units']
            fname = studdict[values['studid']]['fname']
            mname = studdict[values['studid']]['mname']
            lname = studdict[values['studid']]['lname']
            #compute the amount of enrollment
            amount = (float(subdict[values['subid']]['units']) * float(studdict[values['studid']]['rate'])).__round__(2)
            #update the window with the information
            wind['teacher'].update(teacher)
            wind['units'].update(units)
            wind['amount'].update(amount)
            wind['fname'].update(fname)
            wind['mname'].update(mname)
            wind['lname'].update(lname)            
            #newdict[counter] = { 'studid':studid,'subid':subid,'term':term,'amount':enramount}
            newdict['{}{}{}'.format(studid,subid,term)] = { 'studid':studid,'subid':subid,'term':term,'amount':amount}
            olddict.update(newdict)
            print(olddict)
            savefile(olddict)
            wind['message'].update('RECORD SAVED')
            continue



def editenrollment(enrolldict,studdict,subdict):

    
#enrolldict['dj'] = {'term':subdict['BIOLOGY101A']['term'],
#                'teacher':subdict['BIOLOGY101A']['teacher'],
#                'amount': (float(subdict['BIOLOGY101A']['units']) * float(enrolldict['dj']['rate'])).__round__(2)}
    editlayout = [
            [sg.Text('',size=20)],
            [sg.Text('Enrollment Record',size=15,font=('Arial',20)),sg.OptionMenu(enrolldict.keys(),size=50,key='enrollrec')
             ,sg.Submit()],
            [sg.Text('',size=50,font=('Arial',20))],            
            [sg.Text('',size=20,font=('Arial',20))],
            [sg.Text('Student ID',size=10,font=('Arial',20)),sg.OptionMenu(studdict.keys(),size=20,key='studid'),
             sg.Text('',size=20,font=('Arial',20))],
            [sg.Text('Subject ID',size=10,font=('Arial',20)),sg.OptionMenu(subdict.keys(),size=20,key='subid'),
             sg.Text('',size=20,font=('Arial',20))],
            [sg.Text('Term',size=10,font=('Arial',20)),sg.OptionMenu(('TERM012022','TERM022022','TERM032022'),size=20,key='term'),
             sg.Text('',size=20,font=('Arial',20))],
            [sg.Text('Subject Name',size = (20,1),font=('Arial',20)),sg.Text('',key='subname',size = (20,1),text_color='Blue',font=('Arial',20))],
            [sg.Text('Teacher Name',size = (20,1),font=('Arial',20)),sg.Text('',key='teacher',size = (20,1),text_color='Blue',font=('Arial',20))],
            [sg.Text('Units',size = (20,1),font=('Arial',20)),sg.Text('',key='units',size = (20,1),text_color='Blue',font=('Arial',20))],
            [sg.Text('Amount',size = (20,1),font=('Arial',20)),sg.Text('',key='amount',size = (20,1),text_color='Blue',font=('Arial',20))],
            [sg.Text('Student ID',size = (20,1),font=('Arial',20)),sg.Text('',key='studid',size = (20,1),text_color='Blue',font=('Arial',20))],
            [sg.Text('First Name',size = (20,1),font=('Arial',20)),sg.Text('',key='fname',size = (20,1),text_color='Blue',font=('Arial',20))],
            [sg.Text('Middle Name',size = (20,1),font=('Arial',20)),sg.Text('',key='mname',size = (20,1),text_color='Blue',font=('Arial',20))],
            [sg.Text('Last Name',size = (20,1),font=('Arial',20)),sg.Text('',key='lname',size = (20,1),text_color='Blue',font=('Arial',20))],  
            [sg.Text('',key='message',size=50,font=('Arial',20))],         
            [sg.Cancel(font=('Arial',20)),sg.Button('EDIT THIS',font=('Arial',20))]            
            ]
    wind = sg.Window('Enrollment Registration',editlayout)   
    while True:
        event, values = wind.read()
        wind['message'].update('')
        if event == sg.WIN_CLOSED or event == 'Cancel':
            wind.close()
            break  
        elif event == 'Submit':
            #get the values from the tables
            
            #counter = int(mykey[0])
            #print(values['enrollrec'])
            studid = enrolldict[values['enrollrec']]['studid']
            subid = enrolldict[values['enrollrec']]['subid']
            term = enrolldict[values['enrollrec']]['term']
            amount = (float(subdict[subid]['units']) * float(studdict[studid]['rate'])).__round__(2)
            subname = subdict[subid]['subname']
            teacher = subdict[subid]['teacher']
            units = subdict[subid]['units']
            fname = studdict[studid]['fname']
            mname = studdict[studid]['mname']
            lname = studdict[studid]['lname']
            #update the window with the information
            wind['studid'].update(studid)
            wind['subid'].update(subid)
            wind['term'].update(term)
            wind['subname'].update(subname)
            wind['teacher'].update(teacher)
            wind['units'].update(units)
            wind['amount'].update(amount)
            wind['fname'].update(fname)
            wind['mname'].update(mname)
            wind['lname'].update(lname)
            #save the info to dictionary
        elif event == 'EDIT THIS':
                        #get the values from the tables
            
            #counter = int(mykey[0])
            #print(values['enrollrec'])
            studid = enrolldict[values['enrollrec']]['studid']
            subid = enrolldict[values['enrollrec']]['subid']
            term = enrolldict[values['enrollrec']]['term']
            amount = (float(subdict[values['subid']]['units']) * float(studdict[values['studid']]['rate'])).__round__(2)
            subname = subdict[subid]['subname']
            teacher = subdict[subid]['teacher']
            units = subdict[subid]['units']
            fname = studdict[studid]['fname']
            mname = studdict[studid]['mname']
            lname = studdict[studid]['lname']
            #update the window with the information
            wind['studid'].update(studid)
            wind['subid'].update(subid)
            wind['term'].update(term)
            wind['subname'].update(subname)
            wind['teacher'].update(teacher)
            wind['units'].update(units)
            wind['amount'].update(amount)
            wind['fname'].update(fname)
            wind['mname'].update(mname)
            wind['lname'].update(lname)
            newdict ={}
            newdict['{}{}{}'.format(studid,subid,term)] = { 'studid':studid,'subid':subid,'term':term,'amount':amount}
            enrolldict.update(newdict)            
            savefile(enrolldict)
            wind['message'].update('RECORD SAVED')
            continue
        



def deleteenrollment(enrolldict,studdict,subdict):
    sg.theme('Purple')
    editlayout = [
            [sg.Text('',size=20,font=('Arial',20))],
            [sg.Text('Enrollment Record',size=10),sg.OptionMenu(enrolldict.keys(),size=50,key='enrollrec')
             ,sg.Submit()],
            [sg.Text('',size=50)],            
            [sg.Text('',size=20,font=('Arial',20))],
            [sg.Text('Student ID',size=10),sg.OptionMenu(studdict.keys(),size=20,key='studid'),
             sg.Text('',size=20,font=('Arial',20))],
            [sg.Text('Subject ID',size=10),sg.OptionMenu(subdict.keys(),size=20,key='subid'),
             sg.Text('',size=20,font=('Arial',20))],
            [sg.Text('Term',size=10),sg.OptionMenu(('TERM012022','TERM022022','TERM032022'),size=20,key='term'),
             sg.Text('',size=20,font=('Arial',20))],
            [sg.Text('Subject Name',size = (20,1)),sg.Text('',key='subname',size = (20,1),text_color='Blue')],
            [sg.Text('Teacher Name',size = (20,1)),sg.Text('',key='teacher',size = (20,1),text_color='Blue')],
            [sg.Text('Units',size = (20,1)),sg.Text('',key='units',size = (20,1),text_color='Blue')],
            [sg.Text('Amount',size = (20,1)),sg.Text('',key='amount',size = (20,1),text_color='Blue')],
            [sg.Text('Student ID',size = (20,1)),sg.Text('',key='studid',size = (20,1),text_color='Blue')],
            [sg.Text('First Name',size = (20,1)),sg.Text('',key='fname',size = (20,1),text_color='Blue')],
            [sg.Text('Middle Name',size = (20,1)),sg.Text('',key='mname',size = (20,1),text_color='Blue')],
            [sg.Text('Last Name',size = (20,1)),sg.Text('',key='lname',size = (20,1),text_color='Blue')],  
            [sg.Text('',key='message',size=50)],         
            [sg.Cancel(),sg.Button('DELETE THIS')]            
            ]
    wind = sg.Window('Enrollment Registration',editlayout)   
    while True:
        event, values = wind.read()
        wind['message'].update('')
        if event == sg.WIN_CLOSED or event == 'Cancel':
            wind.close()
            break  
        elif event == 'Submit':
            try:
                #get the values from the tables
                
                #counter = int(mykey[0])
                #print(values['enrollrec'])
                studid = enrolldict[values['enrollrec']]['studid']
                subid = enrolldict[values['enrollrec']]['subid']
                term = enrolldict[values['enrollrec']]['term']
                amount = enrolldict[values['enrollrec']]['amount']
                subname = subdict[subid]['subname']
                teacher = subdict[subid]['teacher']
                units = subdict[subid]['units']
                fname = studdict[studid]['fname']
                mname = studdict[studid]['mname']
                lname = studdict[studid]['lname']
                #update the window with the information
                wind['studid'].update(studid)
                wind['subid'].update(subid)
                wind['term'].update(term)
                wind['subname'].update(subname)
                wind['teacher'].update(teacher)
                wind['units'].update(units)
                wind['amount'].update(amount)
                wind['fname'].update(fname)
                wind['mname'].update(mname)
                wind['lname'].update(lname)
                #save the info to dictionary
            except:
                wind['message'].update('Please choose a record')
                continue
        elif event == 'DELETE THIS':
            try:            #get the values from the tables
                enrollkey = values['enrollrec']
                print(enrollkey)

                enrolldict.pop(values['enrollrec'])
                savefile(enrolldict)
                wind['message'].update('Delete Successful')
                continue
            except:
                wind['message'].update('Please choose a record')
                continue


def enrollmain():
    enrolldict ={}
    subdict = {}
    enrolldict ={}

    fileenroll = open('enroll.json','r')
    enrolldict = json.load(fileenroll)
    
    filestud = open('students.json','r')
    studdict = json.load(filestud)
    #print(studdict)

    filesub = open('subjects.json','r')
    subdict = json.load(filesub)
    #print(subdict)


    sg.theme('Purple')
    layout = [  
            [sg.Text('Enrollment Maintenance',justification='center', text_color='Blue',size = 40,font=('Arial',20))],
            [sg.Button('Add Enrollment   ',size=20,key='Add',font=('Arial',20)),sg.Text('Add new records',justification='left',size = (20,1),font=('Arial',20))],
            [sg.Button('Edit Enrollment  ',size=20,key='Edit',font=('Arial',20)),sg.Text('Edit Existing records',justification='left',size = (20,1),font=('Arial',20))],
            [sg.Button('Delete Enrollment',size=20,key='Delete',font=('Arial',20)),sg.Text('Delete Existing records',justification='left',size = (20,1),font=('Arial',20))],
            [sg.Button('View Enrollment  ',size=20,key='View',font=('Arial',20)),sg.Text('View Existing records',justification='left',size = (20,1),font=('Arial',20))],
            [sg.Button('View Tuition',key='ViewClass',font=('Arial',20))],
            [sg.Cancel(size=20,font=('Arial',20)),sg.Text('Cancel ',justification='left', size = (20,1),font=('Arial',20))],
        ]
    wind2 = sg.Window('Registration of Classes of Students', layout)
    while True:
        event, value = wind2.read()
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            wind2.close()
            break
        elif event == 'Add':
            enrolldict = loadfile(enrolldict)
            addenrollment(enrolldict,studdict,subdict)
            continue
        elif event == 'Edit':
            enrolldict = loadfile(enrolldict)
            editenrollment(enrolldict,studdict,subdict)
            continue
        elif event == 'Delete':
            enrolldict = loadfile(enrolldict)
            deleteenrollment(enrolldict,studdict,subdict)
            continue
        elif event == 'View':


            sg.Popup(enrolldict.keys())
            continue
        elif event == 'ViewClass':
            newlist = []
            newlist = print_tuition(enrolldict)








if __name__ == '__main__':
    enrollmain()


