
from tkinter.font import BOLD
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
          
        x = 0
        self.string = ''
        for x in range(len(self.passdict[self.login])):
            self.string += chr(ord(self.passdict[self.login][x:x+1:1]) - self.shift )
            x += 1
            
        return self.string        


    def loadfile(self):
        try:
            if os.path.exists('pass.json'):
                file = open('pass.json','r')
                self.passdict = json.load(file)
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
    sg.theme('Purple')
    clayout = [ 
        [sg.Text('Enter New Login',size=(20,1),font=('Arial',20)),sg.Input(key='-NLogin-',size=(40,3),font=('Arial',20))],
        [sg.Text('Enter New Password',size=(20,1),font=('Arial',20)),sg.Input(key='-NPassword-',password_char='*',size=(40,3),font=('Arial',20))],
        [sg.Text('Enter Admin Login',size=(20,1),font=('Arial',20)),sg.Input(key='-ALogin-',size=(40,3),font=('Arial',20))],
        [sg.Text('Enter Admin Password',size=(20,1),font=('Arial',20)),sg.Input(key='-APassword-',password_char='*',size=(40,3),font=('Arial',20))],
        [sg.Button('Submit',size=(15,1),font=('Arial',20)),sg.Button('Cancel',size=(15,1),font=('Arial',20))]
    ]
    cwind = sg.Window('Create New Password',clayout)
    while True:
        events, values = cwind.read()
        if events == sg.WINDOW_CLOSED or events == 'Cancel':
            cwind.close()
            break
        elif events == 'Submit':   
            try:

                # validate admin
                   
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
            except:
                return
        elif events == 'Cancel':
            
            return
    


def trytologin(values):
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
        [sg.Text('Login  ',size=(15,1),font=('Arial',20)),sg.Input(font=('Arial',20),key='-Login-',size=(40,3))],
        [sg.Text('Password',size=(15,1),font=('Arial',20)),sg.Input(font=('Arial',20),password_char='*',key='-Password-',size=(40,3))],
        [sg.Text(key='Message',text_color='Blue',font=('Arial',20))],
        [sg.Text(),sg.Button('Submit',size=(15,1),font=('Arial',20)),sg.Button('Cancel',size=(15,1),font=('Arial',20)),sg.Button('Create',font=('Arial',20),size=(15,1))],
        [sg.Text()]
    ]
    wind = sg.Window('Password Login',layout)
    initial = 0
    while True:
        events, values = wind.read()
        wind['Message'].update('')
        if events == sg.WIN_CLOSED or events == 'Cancel':
            break
        #elif values['-Login-'] == '' or values['-Password-']=='':
        #    break
        elif events == 'Submit' :
            
            if trytologin(values):
                sg.Popup('Login Successful',font=('Arial',20))
                wind['-Login-'].update('')
                wind['-Password-'].update('')
                wind['Message'].update('')
                main.mainmenu()
                continue
            elif not trytologin(values):
                sg.Popup('Password Incorrect',font=('Arial',20))
                wind['-Login-'].update('')
                wind['-Password-'].update('')
                wind['Message'].udpate('')
                
                continue
            
            elif values['-Password-'] == '' or values['-Login-'] == '':
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