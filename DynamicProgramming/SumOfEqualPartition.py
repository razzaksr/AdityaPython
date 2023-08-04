'''
0 1 2 3
1,2,3,4 >> myList
cumulateSum=10
sumAgainst=5
length=4

myTrack=[
       0     1     2     3    4     5
    [True,False,False,False,False,False],  >> 0
        0     1     2     3    4     5
    [True,False,False,False,False,False],  >> 1
        0     1     2     3    4     5
    [True,False,False,False,False,False],  >> 2
        0     1     2     3    4     5
    [True,False,False,False,False,False],  >> 3
        0     1     2     3    4     5
    [True,False,False,False,False,False]   >> 4
]
'''
def isSumEqualsSub(myList):
    cumulateSum=sum(myList)
    # 2>> odd or even, 2%2 >> 0 ;; 10%2>> 0
    if cumulateSum%2!=0:
        return False
    else:
        sumAgainst=cumulateSum//2   
        length=len(myList)
        
        myTrack=[[False]*(sumAgainst+1) for _ in range(length+1)]
        
        for row in range(length+1):
            myTrack[row][0]=True
        
        for row in range(1, length+1):
            for column in range(1, sumAgainst+1):
                # myList[0]>> 1 > 1
                if myList[row-1]>column:
                    myTrack[row][column]=myTrack[row-1][column]
                else:
                    # or >> True or False >> True, False or True>> True, True or True >> True, False or False >> False
                    # 1,1           = 0,1 or 0,0>> 
                    myTrack[row][column]=myTrack[row-1][column] or myTrack[row-1][column-myList[row-1]]
        
        return myTrack[length][sumAgainst]

result=isSumEqualsSub([1,2,3,4])
print(result)

result=isSumEqualsSub([2,3,4,6])
print(result)