import os
import json



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
    #   s = Students('S7484717Z','Jose','Diestro','Ibay',1200.00)
    #studdict = {'studid':[],'fname':[],'mname':[],'lname':[],'rate':[]}
    rate = 0.00
    newstuddict = {}
    print('#################################################################')
    print('#######################   Add Students  #########################')
    studid = input('#  Enter the Student ID   : ')
    fname =  input('#  Enter the First Name   : ')
    mname =  input('#  Enter the Middle Name  : ')
    lname =  input('#  Enter the Last Name    : ')
    rate  =  input('#  Enter the Tuition Rate : ') 
    #load the existing dict
    #studdict = loadfile('students.json',studdict)
    newstuddict[studid]={'fname':fname,'mname':mname,'lname':lname,'rate':rate}
    studdict.update(newstuddict)
    print(studdict)
    #save the added items    
    savefile(studdict)
    with open('students.json','w') as f3:
        studdict = json.dump(studdict,f3 )
        print('added to students')
    return studdict


    



def editstudents(studdict):
    print('#################################################################')
    print('#######################  Edit Students  #########################')
    studid = input('#  Enter the Student ID   : ')
    try: 
        if studid in studdict:
        
    #print(len(studdict))
    #ctr =0
            newstudid = input('#  Enter NEW Student ID   : ')
            fname =  input('#  Enter NEW First Name   : ')
            mname =  input('#  Enter NEW Middle Name  : ')
            lname =  input('#  Enter NEW Last Name    : ')  
            rate =   input('#  Enter NEW Rate         : ')    

#studid SKDJHH4J4 key, value[0]
#fname Plant
#mname Based
#lname Cactus
#rate 2233.23
        if newstudid == studid:
            nstuddict ={}
            nstuddict[studid]={'fname':fname,'mname':mname,'lname':lname,'rate':rate}
            studdict.update(nstuddict)
            savefile(nstuddict)
            return nstuddict
        else :        
            nstuddict ={}
            nstuddict[newstudid]={'fname':fname,'mname':mname,'lname':lname,'rate':rate}
            studdict.update(nstuddict)
            studdict.pop(studid)
            savefile(studdict)
        return studdict
    except :
        return

def deletestudents(studdict):
    nstuddict = studdict
    print('#################################################################')
    print('####################### Delete Students  #########################')
    studid = input('#  Enter the Student ID   : ')
    if studid == '':
        return
    nstuddict.pop(studid)
    savefile(nstuddict)
    return nstuddict


def studmain():
    studdict = {None:None}
    subdict = {}
    enrolldict = {}
    if not os.path.exists('students.json'):
        fx = open('students.json','w')
        json.dump(studdict,fx)
        fx.close()
    else :
        studdict = loadfile(studdict)
    
    while True:
        print()
        print()
        print('#################################################################')
        print('############### Student Maintenance Program  ####################')
        print('#                     a    add students                         #')
        print('#                     e    edit students                        #')
        print('#                     d    delete students                      #')
        print('#                     v    view the students                    #')
        print('#                     q    cancel                               #')
        print('#################################################################')
        mychoice = input('#         Enter your choice : ')
        print('#################################################################')
        if mychoice == '':
            continue
        elif mychoice in 'aA':
            print('add students')
            addstudents(studdict)
        elif mychoice in 'eE':
            print('edit students')
            editstudents(studdict)
        elif mychoice in 'dD':
            print('delete students')
            deletestudents(studdict)
        elif mychoice in 'Vv':
            df = pd.DataFrame.from_dict(studdict)

            print('view students')
            #print(studdict)
            print(df)
            df = ''
            #print(df)
        elif mychoice in 'Qq':
            break
        else : continue
    studdict = {}
    subdict = {}
    enrolldict = {}
    df = ''

if __name__ == '__main__':
    studmain()
    studdict = {}
    subdict = {}
    enrolldict = {}
    #studdict = {'studid':[],'fname':[],'mname':[],'lname':[],'rate':[]}
    #savefile(studdict)
    print(studdict)