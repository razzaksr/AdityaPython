#O(n)
def sumOfTwo(myList,myTarget):
    myList.sort()
    #print(myList)
    min,max=0,len(myList)-1
    while min<max:
        sum=myList[min]+myList[max]
        if sum==myTarget:
            print("Pair found ",myList[min],myList[max])
            return
        elif sum<myTarget:
            min=min+1
        else:
            max=max-1;
    else:
        print("Pair not found")
    
#sumOfTwo([8,4,12,6],11)

hold,data=19,10

print(hold,data)

hold,data=data,hold
# hold+=data
# data=hold-data
# hold-=data

# cosmo=hold
# hold=data
# data=cosmo

print(hold,data)