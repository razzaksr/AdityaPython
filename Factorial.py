def factorial(number):
    if number==1 or number==0:
        return 1
    else:
        return number*factorial(number-1)
    
fact=factorial(int(input("Enter the number to find factorial ")))
print(fact)