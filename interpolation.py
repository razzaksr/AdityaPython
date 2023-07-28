def searchInterpol(myList, target):
    if not myList:
        print("Invalid list")
        return -1
    (left,right)=(0,len(myList)-1)
    while myList[left]!=myList[right] and myList[left]<=target<=myList[right]:
        mid=left+((target-myList[left]))*(right-left)//(myList[right]-myList[left])
        
        if target==myList[mid]:
            return mid
        elif target>myList[mid]:
            left=mid+1
        else:
            right=mid-1
    
    if target==myList[left]:
        return left
    
    print(target,"Not found")
    return -1 # not found desired element in the list

position=searchInterpol([5,10,12,22,45,89],11)
print(position)