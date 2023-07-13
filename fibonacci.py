# num1,num2,sum=0,1,0
# # 7
# length=int(input("Enter the length of fibonacci you required....."))
# if length<2:
#     print("Invalid length to generate fibonacci")
# else:
#     print(num1)
#     print(num2)
#     length-=2 # 5
#     while length>0:
#         sum=num1+num2
#         print(sum)
#         num1=num2
#         num2=sum
#         length-=1;

#Optimized Fibonacci 

def fiboOptimized(length):
    if length<=0:
        return []
    elif length==1:
        return [0]
    elif length==2:
        return [0,1]
    else:
        seriesList=fiboOptimized(length-1)
        seriesList.append(seriesList[-1]+seriesList[-2])
        return seriesList

myList=fiboOptimized(5)
print(myList)

