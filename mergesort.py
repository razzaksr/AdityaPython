def sortMerge(myList):
    if len(myList)>1:
        mid=len(myList)//2
        # list[start:end]
        leftList=myList[:mid]
        rightList=myList[mid:]
        
        sortMerge(leftList)
        sortMerge(rightList)
        
        leftPos=rightPos=index=0
        
        while leftPos<len(leftList) and rightPos<len(rightList):
            if leftList[leftPos]<rightList[rightPos]:
                myList[index]=leftList[leftPos]
                leftPos+=1
            else:
                myList[index]=rightList[rightPos]
                rightPos+=1
            index+=1
            
        while leftPos<len(leftList):
            myList[index]=leftList[leftPos]
            leftPos+=1
            index+=1
        while rightPos<len(rightList):
            myList[index]=rightList[rightPos]
            rightPos+=1
            index+=1
            
myData=["Spring","Express","Hibernate","Mongoose","DJango","Node","Flask"]
print(myData)
sortMerge(myData)
print(myData)