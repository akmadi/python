'''
Created on Nov 30, 2017

@author: amadin001c


'''


list = ['test','king','kill']
list.sort()
print(list[0])

list.reverse();

print(list[2])


number = int (input("Enter number"))

if (number%2==0):
    print("This is an even number")
elif (number%2==1):
    print("This is an odd number")
else:
    print("Number is not valid")
    
    
    
def hello():
        print("This is a sample method!!!")
        print("Sample line inside method")
        
hello()