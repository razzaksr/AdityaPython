def bubbleSort(myList):
    for times in range(len(myList)-1):
        for bubble in range(len(myList)-times-1):
            if myList[bubble]<myList[bubble+1]:
                myList[bubble],myList[bubble+1]=myList[bubble+1],myList[bubble]


myData=[89,34,12,56,11]
bubbleSort(myData)
print(myData)