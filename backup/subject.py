import os
import json
import pandas as pd


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
    print('#################################################################')
    print('#######################   Add Subjects  #########################')
    subid = input('#  Enter the Subject ID   : ')
    if subid == '':
        return
    if subid in subdict:
        print('existing subject')
    else :
        subname =  input('#  Enter the Subject Name : ')
        teacher =  input('#  Enter the Teacher Name : ')
        term =     input('#  Enter the TERM Code    : ')
        units =    input('#  Enter the UNITS        : ')
    
        subdict[subid] = {'subname': subname,
                    'teacher': teacher,
                    'term': term,
                    'units' : units}

        with open('subjects.json','w') as a3:
            json.dump(subdict,a3 )
            a3.close()
        print('added to students')
    return subdict


    



def editsubjects(subdict):
    newsubdict = {None:None}
    print('#################################################################')
    print('#######################  Edit Subjects  #########################')
    subid = input('#  Enter the Subject ID   : ')

    try:    


        if subid in subdict:
            newsubid = input('#  Enter NEW Subject ID   : ')
            subname =  input('#  Enter NEW Subject Name : ')
            teacher =  input('#  Enter NEW Teacher Name : ')
            term =     input('#  Enter NEW TERM Code    : ') 
            units =    input('#  Enter the UNITS        : ')
        if newsubid == subid :
            if not subname == subdict[subid]['subname']:
                subdict[subid]['subname'] = subname 
            if not teacher == subdict[subid]['teacher']:
                subdict[subid]['teacher']= teacher
            if not term == subdict[subid]['term']:
                subdict[subid]['term']= term
            if not units == subdict[subid]['units']:
                subdict[subid]['units'] = units
            savefile(subdict)
            return subdict
        else :    
            newsubdict = {newsubid :  {'subname': subname,
                        'teacher': teacher,
                        'term': term,
                        'units' : units}}    
            
            subdict.update(newsubdict)
            subdict.pop(subid)
            savefile(subdict)
            return subdict
    except:
        return

def deletesubjects(subdict):
    nsubdict = subdict
    print('#################################################################')
    print('####################### Delete Subject  #########################')
    subid = input('#  Enter the Subject ID   : ')
    if subid == '':
        return
    nsubdict.pop(subid)
    nsubdict.update(nsubdict)
    savefile(nsubdict)
    return nsubdict


def submain():
    studdict = {}
    subdict = {None:None}
    enrolldict = {}
    if not os.path.exists('subjects.json'):
        a4 = open('subjects.json','w')
        json.dump(subdict,a4)
        a4.close()
    else :
        subdict = loadfile(subdict)

    while True:
        print()
        print()
        print('#################################################################')
        print('############### Subject Maintenance Program  ####################')
        print('#                    a    add subjects                          #')
        print('#                    e    edit subjects                         #')
        print('#                    d    delete subjects                       #')
        print('#                    v    view the subjects                     #')
        print('#                    q    cancel                                #')
        print('#################################################################')
        mychoice = input('#         Enter your choice : ')
        print('#################################################################')
        if mychoice == '':
            continue
        elif mychoice in 'aA':
            print('add students')
            subdict = addsubjects(subdict)
        elif mychoice in 'eE':
            print('edit students')
            subdict = editsubjects(subdict)
        elif mychoice in 'dD':
            print('delete students')
            subdict = deletesubjects(subdict)
        elif mychoice in 'Vv':
            df = pd.DataFrame.from_dict(subdict)
            print(df)

        elif mychoice in 'Qq':
            break
        else : continue

if __name__ == '__main__':
    submain()
    subdict = {}
    print(subdict)

