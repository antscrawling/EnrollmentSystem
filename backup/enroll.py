import json
import os
from re import sub
import pandas as pd

def writetofile(thisdict):
    #print(enrolldict)
    #f3 = open('enroll.json','w')
    #json.dump(enrolldict,f3)
    pass

def addenrollment():
    pass
#enrolldict['dj'] = {'term':subdict['BIOLOGY101A']['term'],
#                'teacher':subdict['BIOLOGY101A']['teacher'],
#                'amount': (float(subdict['BIOLOGY101A']['units']) * float(enrolldict['dj']['rate'])).__round__(2)}


def editenrollment():
    pass
#enrolldict['dj'] = {'term':subdict['BIOLOGY101A']['term'],
#                'teacher':subdict['BIOLOGY101A']['teacher'],
#                'amount': (float(subdict['BIOLOGY101A']['units']) * float(enrolldict['dj']['rate'])).__round__(2)}

def deleteenrollment():
    pass

def enrollmain():
    enrolldict ={}
    subdict = {}
    enrolldict ={None:None}

    if os.path.exists('enroll.json'):
        c1 = open('enroll.json','r')
        enrolldict = json.load(c1)
    else : 
        c1 = open('enroll.json','w')
        json.dump(enrolldict,c1)
    print(subdict)
    print(enrolldict)
    print(enrolldict)
    while True:
        print('#################################################################')
        print('###############      Enroll A Student        ####################')
        print('                  a    add students enrollment')
        print('                  e    edit students enrollment')
        print('                  d    delete students enrollment')
        print('                  v    view the students enrollment')
        print('                  q    cancel')
        thischoice = input('Enter choice : ')
        if thischoice in 'aA':
            addenrollment()
        elif thischoice in 'eE':
            editenrollment()
        elif thischoice in 'dD':
            deleteenrollment()
        elif thischoice in 'Vv':
            df = pd.DataFrame.from_dict(enrolldict)
            print(df)
            df = ''
        elif thischoice in 'Qq':
            break
        elif thischoice == '':
            continue       





if __name__ == '__main__':
    enrollmain()


