from sys import *
def linear(myList):
    min=max=myList[0]
    
    for current in myList:
        if current>max:
            max=current
        if current<min:
            min=current
    
    print(min,"is min value and ",max,"is max value")
    
# maxsize=1000000000, -maxsize=-100000000
# min=maxsize, max=-maxsize
def divideNConquer(myList,left,right,min=maxsize,max=-maxsize):
    if left == right:
        if min>myList[right]:
            min=myList[right]
        if max<myList[left]:
            max=myList[left]
        return min, max
    if right - left == 1:
        if myList[left] < myList[right]:
            if min > myList[left]:
                min=myList[left]
            if max < myList[right]:
                max=myList[right]
        else:
            if min>myList[right]:
                min=myList[right]
            if max<myList[left]:
                max=myList[left]
        return min, max
    
    mid=(left+right)//2
    
    min, max = divideNConquer(myList,left,mid,min,max)
    
    min, max = divideNConquer(myList,mid+1,right,min,max)
    
    return min, max

myData=[4.5,2.3,9.2,0.012,5.6,0.89]
#linear(myData)

#tuple=more than one returns
(least,largest)=divideNConquer(myData,0,len(myData)-1)
print("Min value is",least,"max value is",largest)