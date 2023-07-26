def heapify(myList, length, parent):
    maximum=parent
    left=2*parent+1
    right=2*parent+2
    if left<length and myList[left]>myList[maximum]:
        maximum=left
    if right<length and myList[right]>myList[maximum]:
        maximum=right
    
    if parent!=maximum:
        myList[maximum],myList[parent]=myList[parent],myList[maximum]
        heapify(myList,length,maximum)

def heapSort(myList):
    for begin in range(len(myList)//2-1,-1,-1):
        heapify(myList,len(myList),begin)
    for position in range(len(myList)-1,0,-1):
        myList[0],myList[position]=myList[position],myList[0]
        heapify(myList,position,0)
        
myData=[89,12,56,11,34]
heapSort(myData)
print(myData)