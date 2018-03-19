'''
Created on Dec 26, 2017

@author: amadin001c
'''

'''class MyClass(object):
    
    classdocs
    
    
    '''
    
    
def main():
    list = [1,3,6,4,5,2,4]
    item=4
    result = binarysort(list, item)
    print('position is '+str(result))

def binarysort(list,item):
        
        min = 0
        max = len(list)
        mid = int((min+max)/2)
        
        list.sort(key=None, reverse=False)
        for x in range (min,max):
            if list[mid] < item:
                min = mid
                mid = int((min+max)/2)
            elif list[mid] > item:
                max = mid
                mid = int((min+max)/2)
            else:
                result = mid
    
        return result
    
    
    
    
    
if __name__ == '__main__':
  main()  
    
      
