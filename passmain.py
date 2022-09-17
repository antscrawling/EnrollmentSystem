
import main
import os
import json
import PySimpleGUI as sg


class thispass:
    def __init__(self,login,password,shift) -> None:
        self.login = login
        self.password = password
        self.shift = shift
        self.passdict = {}
        self.string = ''

    def encrypt(self):
        x = 1
        self.passdict[self.login] = self.password
        for x in range(len(self.password)):
            self.string += chr(ord(self.password[x:x+1:1]) + self.shift )
            x += 1
        return self.string 

    def decrypt(self):
        newdict = {}
        x = 0
        self.string = ''
        for x in range(len(self.passdict[self.login])):
            self.string += chr(ord(self.passdict[self.login][x:x+1:1]) - self.shift )
            x += 1
            #print(self.string)
        return self.string        


    def loadfile(self):
        try:
            if os.path.exists('pass.json'):
                file = open('pass.json','r')
                self.passdict = json.load(file)
                print('File saved')
                file.close()   
        except:
            self.savefile()
        return self.passdict

    def savefile(self):
        file = open('pass.json','w')
        json.dump(self.passdict,file)
        file.close()

    def is_pass_true(self,login,password):
        if self.passdict[login] == password:
            return True



def createpass():
    

    
    thisdict = {}
    sg.theme('Purple')
    clayout = [ 
        [sg.Text('Enter New Login',size=(20,1),font='Arial'),sg.Input(key='-NLogin-',size=(40,3),font='Arial')],
        [sg.Text('Enter New Password',size=(20,1),font='Arial'),sg.Input(key='-NPassword-',size=(40,3),font='Arial')],
        [sg.Text('Enter Admin Login',size=(20,1),font='Arial'),sg.Input(key='-ALogin-',size=(40,3),font='Arial')],
        [sg.Text('Enter Admin Password',size=(20,1),font='Arial'),sg.Input(key='-APassword-',size=(40,3),font='Arial')],
        [sg.Button('Submit',size=(15,1),font='Arial'),sg.Button('Cancel',size=(15,1),font='Arial')]
    ]
    cwind = sg.Window('Create New Password',clayout)
    while True:
        events, values = cwind.read()
        if events == sg.WINDOW_CLOSED or events == 'Cancel':
            cwind.close()
            break
        #elif values['-Nlogin-'] == '' or values['-ALogin-'] == '' or values['-NPassword-'] == '' or values['-APassword-'] == '':
        #    cwind.close()
        #    break
        elif events == 'Submit':   
            try:

                # validate admin
                storeddict = {}
                shift = len(values['-ALogin-']+values['-APassword-']) * 2 
                oldpass = thispass(values['-ALogin-'],values['-APassword-'],shift)
                oldpass.passdict = oldpass.loadfile()
                adminpass = oldpass.decrypt()
                # check if pass is the same
                if adminpass == values['-APassword-']:
                    print('success login to admin')
                    shift = len(values['-NLogin-']+values['-NPassword-']) * 2 
                    newpass = thispass(values['-NLogin-'],values['-NPassword-'],shift)
                    epass = newpass.encrypt()
                    newpass.passdict = {values['-NLogin-']:epass}
                    oldpass.passdict  = oldpass.loadfile()
                    oldpass.passdict.update(newpass.passdict)
                    oldpass.savefile()
                    cwind.close()
                    return
                else:
                    cwind.close()
                    break

                #shift = len(values['-NLogin-']+values['-NPassword']) * 2 
                #createpass = thispass(values['-NLogin-'],values['-NPassword'],shift)      
                #createpass.passdict = createpass.loadfile()
                #epass = createpass.encrypt()


                #createpass.passdict = createpass.loadfile()
                #createpass.passdict.update(thisdict)
                #createpass.savefile()
                #print(createpass.passdict)
            except:
                return
    #mypass.decrypt()
        elif events == 'Cancel':
            
            return
    
    #print(mypass.passdict)

def trytologin(values):
    entereddict = {}
    
    #login = input('Enter Saved Login : ')
    #password = input ('Enter Saved Password : ')  
    shift = len(values['-Login-']+values['-Password-']) * 2 
    mypass = thispass(values['-Login-'],values['-Password-'],shift)  
    mypass.passdict = mypass.loadfile()
    savedpass = mypass.decrypt()
    if savedpass == values['-Password-'] :
        print('login successful')
        #createpass()
        return True
    else:
        print('Login unsuccessful')
        return False


def deletelogin(values):
    

    login = input('Enter Admin ID :')
    password = input ('Enter Admin Password : ')  
    if login == '' or password == '':
        return
    shift = len(login+password) * 2 
    dpass = thispass(login,password,shift)  
    dpass.passdict = dpass.loadfile()
    savedpass = dpass.decrypt()
    if savedpass == password :
        print('login successful')
        dlogin = input('Enter Login to delete : ')
        if dlogin == '' : return
        try:
            if dlogin in dpass.passdict.keys():
                dpass.passdict.pop(dlogin)
                dpass.savefile()
                print('login deleted')
        except: return
    else:
        print('Login unsuccessful')






def passmain():
    sg.theme('Purple')
    layout = [ 
        [sg.Text()],
        [sg.Text('Login  ',size=(15,1),font='Arial'),sg.Input(font='Arial',key='-Login-',size=(40,3))],
        [sg.Text('Password',size=(15,1),font='Arial'),sg.Input(font='Arial',key='-Password-',size=(40,3))],
        [sg.Text(key='Message')],
        [sg.Button('Submit',size=(15,1),font='Arial'),sg.Button('Cancel',size=(15,1),font='Arial'),sg.Button('Create',font='Arial',size=(15,1))],
        [sg.Text()]
    ]
    wind = sg.Window('Password Login',layout)
    while True:
        events, values = wind.read()
        wind['Message'].update('')
        if events == sg.WIN_CLOSED or events == 'Cancel':
            break
        #elif values['-Login-'] == '' or values['-Password-']=='':
        #    break
        elif events == 'Submit' :
            try:
                if trytologin(values):
                    sg.Popup('Login Successful')
                    wind['-Login-'].update('')
                    wind['-Password-'].update('')
                    wind['Message'].update('')
                    main.mainmenu()
                    continue
                else:
                    sg.Popup('Password Incorrect')
                    wind['-Login-'].update('')
                    wind['-Password-'].update('')
                    wind['Message'].udpate('')
                    continue
            except: 
                wind['Message'].update('Blank entered')
                continue
        elif events == 'Create':            
            createpass()
            continue
            



if __name__ == '__main__':
    global frommain 
    frommain = True
    passmain()
    #createpass()
    #trytologin()