def sort(myList,start,end):
    pivotalData=myList[end]
    initial=start-1
    
    for current in range(start,end):
        if myList[current]<pivotalData:
            initial+=1
            myList[current],myList[initial]=myList[initial],myList[current]
    
    myList[end],myList[initial+1]=myList[initial+1],myList[end]
    
    return initial+1

def quick(myList,start,end):
    if start<end:
        pivotalPoint=sort(myList,start,end)
        
        quick(myList,start,pivotalPoint-1)
        quick(myList,pivotalPoint+1,end)
        
myData=[8.9,12.8,1.1,9.0,45.1,2.3]
quick(myData,0,len(myData)-1)
print(myData)