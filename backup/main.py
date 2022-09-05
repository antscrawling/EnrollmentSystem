
import stud
import subject
import enroll


def main():
    while True:
        print('#################################################################')
        print('###############      Enrollment Program      ####################')
        print('#                     s students                                #')
        print('#                     c subjects                                #')
        print('#                     e enrollment                              #')
        print('#                     q to quit                                 #')
        print('#################################################################')
        thischoice = input('#         Enter choice : ')
        print('#################################################################')
        if thischoice in 'sS':
            stud.studmain()
        elif thischoice in 'Cc':
            subject.submain()
        elif thischoice in 'eE':
            enroll.enrollmain()
        elif thischoice in 'Qq':
            break
        elif thischoice == '':
            continue     


if __name__ == '__main__':
    main()



