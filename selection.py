# O(n)
def selection(myList):
    current=0
    while current<len(myList)-1:
        #print(myList[current],myList[current+1])
        if myList[current]<myList[current+1]:
            myList[current],myList[current+1]=myList[current+1],myList[current]
            current=-1
        current+=1
        

#O(n2)
def selectSort(myList):
    for hold in range(0,len(myList)):
        for compare in range(hold+1,len(myList)):
            if myList[hold]>myList[compare]:
                myList[hold],myList[compare]=myList[compare],myList[hold]


myData=[14,32,26,43,19]
#selection(myData)
selectSort(myData)
print(myData)