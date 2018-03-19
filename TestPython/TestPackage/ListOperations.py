'''
Created on Feb 2, 2018

@author: amadin001c
'''
from pip._vendor.distlib.compat import raw_input

def main():
    l = []
    n= int(input())
    for _ in range(n):
        s = raw_input().split()
        cmd = s[0]
        args = s[1:]
        if cmd!="print":
            cmd += "("+",".join(args)+")"
            eval("l."+cmd)
        else:
            print(l)
   
if __name__ == '__main__':
    main()