from sys import *
#[7, 5, 1, 6, 8]
'''
mp=5-7>>-2 , cp=-100000000
0   1    2   3   4
7   5    1   6   8
cb  cs
    i >> 5-7>> -2>> cp
0   1    2   3   4
7   5    1   6   8
   cb    cs
         i>> 1-2 >> -1>> cp , mp=-1

0   1    2   3   4
7   5    1   6   8
   cb       cs
             i>>6-5>>1>> cp>> mp

0   1    2   3   4
7   5    1   6   8
   cb            cs
                 i>>8-5>>3>> cp>> mp
                 
                 8>>mp
                 


'''
def buyAndSell(myList):
    if myList==None or len(myList)<2:
        return "Invalid Stock"
    else:
        currentBuy=myList[0]# 7
        currentSell=myList[1]# 5
        
        maxProfit=currentSell-currentBuy;# 5-7 >> -2
        
        currentProfit=-maxsize;# -100000000
        
        for index in range(1,len(myList)):
            currentProfit=myList[index]-currentBuy;# -2
            
            # -1>-2
            if currentProfit>maxProfit:
                maxProfit=currentProfit
                currentSell=myList[index]
            # 7>5
            if currentBuy > myList[index]:
                currentBuy=myList[index]
        
        finalOutcome=currentSell-maxProfit,currentSell;
        
        return finalOutcome

history=buyAndSell([7, 5, 1, 6, 8])
print(history)

history=buyAndSell([90,45,20,10,2])
print(history)