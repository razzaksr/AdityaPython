# only possibility count
def findPossibilities(stairs):
    if stairs<=0:
        return "Invalid stairs count"
    if stairs==1:
        return 1
    #existing possibility
    myPossibilities=[0]*(stairs+1)
    
    myPossibilities[1]=1
    myPossibilities[2]=2
    
    for current in range(3, stairs+1):
        myPossibilities[current]=myPossibilities[current-1]+myPossibilities[current-2]
    
    return myPossibilities
    
# print all the possibilities 
def showPossibilities(stairs):
    if stairs<=0:
        return "can't generate climb possibility"
    
    #initialize the nest list for every possibility
    myPossibilities=[[] for _ in range(stairs+1)]
    
    myPossibilities[0].append([])
    myPossibilities[1].append([1])
    
    for current in range(2, stairs+1):
        for first in myPossibilities[current-1]:
            myPossibilities[current].append(first+[1])
        for second in myPossibilities[current-2]:
            myPossibilities[current].append(second+[2])
    
    return myPossibilities[stairs]

myStairs=int(input("Enter the no of stairs "))
#myPossy=findPossibilities(myStairs)
myPossy=showPossibilities(myStairs)
for pos in myPossy:
    print(pos)