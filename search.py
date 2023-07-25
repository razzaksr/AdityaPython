myList=[9.2,45.9,12.6,21.8,6.7,34.5]

# O(n)
def linear(myDesired):
    for index in range(len(myList)):
        if myList[index]==myDesired:
            return index
    else:
        return "Not"

# O(logn)
def binary(myDesired,start=0,end=len(myList)-1):
    if start<=end:
        mid=start+(end-start)//2
        if myList[mid]==myDesired:
            return mid
        elif myList[mid]>myDesired:
            return binary(myDesired,start,mid-1)
        else:
            return binary(myDesired,mid+1,end)
    else:
        return "Not"
    
myData=float(input("Enter the desired data to find int he list..."))
#position=linear(myData)
myList.sort()
position=binary(myData)
print(position," where",myData," is exists")