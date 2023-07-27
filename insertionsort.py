def sortInsertion(myList):
    for current in range(1,len(myList)):
        holded=myList[current]
        
        previous=current-1
        
        while previous>=0 and holded>myList[previous]:
            myList[previous+1]=myList[previous]
            previous-=1
        myList[previous+1]=holded
        
myData=[4.5,2.3,9.2,0.012,5.6,0.89]
print(myData)
sortInsertion(myData)
print(myData)