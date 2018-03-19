'''
Created on Dec 27, 2017

@author: amadin001c
'''


def main():
    message = "Call me at 523-456-7890, if i am not available then call me at '510-543-5445'"
    for i in range (len(message)):
        text = message[i:i+12]
        if verifyPhoneNum(text):
            print ("Phone number found: "+text)
    print("Done")
    
def verifyPhoneNum(text):
    if (len(text)!=12):
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
        if text[0] == "1":
            return False
    if (text[3]!='-'):
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if (text[7]!='-'):
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True     


if __name__ == '__main__':
    main()