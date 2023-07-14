def selection(myList):
    current=0
    while current<len(myList)-1:
        #print(myList[current],myList[current+1])
        if myList[current]<myList[current+1]:
            myList[current],myList[current+1]=myList[current+1],myList[current]
            current=-1
        current+=1


myData=[14,32,26,43,19]
selection(myData)
print(myData)