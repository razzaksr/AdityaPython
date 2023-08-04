def withdraw(available,expected):
    myTrack=[float('inf')]*(expected+1)
    
    myTrack[0]=0;
    
    for coin in available:
        for index in range(coin, expected+1):
            myTrack[index]=min(myTrack[index],myTrack[index-coin]+1)
    
    if myTrack[expected]!=float('inf'):
        return myTrack[expected]
    else:
        return -1

result=withdraw([1,2,5],7)
print(result)

result=withdraw([5],23)
print(result)