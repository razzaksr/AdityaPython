def dpFibonacci(number):
    if number<=0:
        return "can't generate fibonacci for "+number
    else:
        mySeries=[0,1]
        
        for count in range(2,number):
            mySeries.append(mySeries[count-1]+mySeries[count-2])
        return mySeries
    
myNumber=int(input("Enter the number to generate fibonacci "))
fiboSeries=dpFibonacci(myNumber)
print(fiboSeries)