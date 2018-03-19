'''
Created on Dec 27, 2017

@author: amadin001c
'''
import re
import os


def main():
    message = "Call me at 523-456-7890, if i am not available then call me at '510-543-5445'"
    text = re.compile('\d\d\d-\d\d\d-\d\d\d\d')
    mobileno = text.search(message)
    print(mobileno.group())
    member = re.compile(r'[^a-zA-Z0-9]')
    vowels = member.findall('Robocop eats baby food. BABY FOOD.')
    print(vowels)
    writeFile = open(os.getcwd()+'\\resources\\TestFile','w')
    writeFile.write('This is a write line!!!!\n and the next line')
    writeFile.close()
    file = open(os.getcwd()+'\\resources\\TestFile')
    content = file.read()
    print(content)
    
    

if __name__ == '__main__':
    main()