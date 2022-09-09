import json
import os
class thispass:
    def __init__(self,key,login,password) -> None:
        self.key1 = key
        self.key2 = key 
        self.login = login
        self.password = password
        self.passdict = {}
        self.charData = []
        self.myord = ''
        self.mysavelist =[]
        self.decriptlist = []
        self.word = ''

    def encrypt(self):
        #'this%is%it
        self.key2 = self.key1.replace(" ","%")
        #'Joseijj6640$_this%is%it'
        self.password = '{}_{}'.format(self.password,self.key2)
        #'J', 'o', 's', 'e', 'i', 'j', 'j', '6', '6', '4', '0', '$', '_', 't', 'h', 'i', 's', '%', 'i', 's', '%', 'i', 't'
        self.charData = list(self.password)
        #print(self.charData)
        #print(self.charData)
        for x in range(len(self.charData)):
            #74, 111, 115, 101, 105, 106, 106, 54, 54, 52, 48, 36, 95, 116, 104, 105, 115, 37, 105, 115, 37, 105, 116
            self.myord = ord(self.charData[x])
            #became a list
            self.mysavelist.append(self.myord)
        self.passdict[self.login] = self.mysavelist
        return self.passdict #regurn a dict

    def decrypt(self,thelist):
        for x in range(len(thelist)):
            self.decriptlist.append(chr(thelist[x]))
        for x in range(len(self.decriptlist)):
            self.word += self.decriptlist[x]
        self.word = self.word.replace('%'," ")
        return self.word  #return a string

def loadfile(studdict):
    #studdict = {'studid':[],'fname':[],'mname':[],'lname':[],'rate':[]}
    with open('pass.json','r') as f1:
        studdict = json.load(f1)
        print('loaded the {} file'.format(f1))
        f1.close()
    return studdict

def savefile(studdict):
    with open('pass.json','w') as f2:
        json.dump(studdict,f2)
        f2.close()
    return studdict


def addnewpassword():   
    #ask for login details
    mylogin = input('Enter your Login Name  : ')
    mypassword = input('Enter your password : ')    
    mykey = input("Enter a paraphrase (Please don't forget this): ")

    #create the class attributes
    passclass = thispass(mykey,mylogin,mypassword)
    #get the dictionary of the password. encryptpassword is a dictionary with key = login
    encryptpassword={}
    encryptpassword = passclass.encrypt()
    print(encryptpassword)
    loadeddict ={}
    #save the dict to json
    if os.path.exists('pass.json'):
        loadeddict = loadfile(loadeddict)
        if mylogin in loadeddict.keys():
            print('This login exists')
            return
        else :
            encryptpassword.update(loadeddict)
            savefile(encryptpassword)
    else :
        savefile(encryptpassword)


def checkpassword(encryptpassword,mypassword,mykey):
    passclass = thispass

    #print(encryptpassword['antscrawling'])
    #decryptpassword is a string
    decryptpassword = passclass.decrypt(encryptpassword,encryptpassword[mykey])

    print(decryptpassword)

    if not decryptpassword == (mypassword+'_'+mykey):
        print("Password the same")


def passmain():
    addnewpassword()
    loaddict = {}
    loaddict = loadfile(loaddict)
    checkpassword(loaddict,'jj6640$','antscrawling')

if __name__ == '__main__':
    passmain()

#Enter your Login Name  : antscrawling
#Enter your password : jj6640$
#Enter a paraphrase (Please don't forget this): this is it
#{'antscrawling': [106, 106, 54, 54, 52, 48, 36, 95, 116, 104, 105, 115, 37, 105, 115, 37, 105, 116]}
#jj6640$_this is it