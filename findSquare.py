def basic(number):
    
    original=number
    # change negative to positive
    number=abs(number)
    
    oddValue=1
    square=0
    
    while number>0:
        square+=oddValue
        oddValue+=2
        number-=1
    
    print(square,"sqaure of",original)
    
#basic(int(input("Enter the number to find square ")))

# shifting operators: 
# left >> 
# right <<

'''
Bitwise : int

4096 2048 1024 512 256 128 64 32 16 8 4 2 1
   0    0    0   0   0   0  0  1  1 1 0 0 0 >> carter
   0    0    0   0   0   1  1  1  0 0 0 0 0 >> 224
   
   0    0    0   0   0   1  0  0  0 0 0 1 0 >> paul
   0    0    0   0   0   0  0  0  0 1 0 0 0 >> 8


'''

# carter=56
# print(carter<<2)
# paul=130
# print(paul>>4)

def optimizedSquare(number):
    if number<2:
        return number
    number=abs(number)
    current=number>>1
    if (number&1)==1:
        return (optimizedSquare(current)<<2)+(current<<2)+1
    else:
        return optimizedSquare(current)<<2
    
value=optimizedSquare(7)
print(value)

'''
4096 2048 1024 512 256 128 64 32 16 8 4 2 1
  0    0     0   0   0   0  0  0  0 0 1 1 1 >> 7
  0    0     0   0   0   0  0  0  0 0 0 0 1 >> 1
  0    0     0   0   0   0  0  0  0 0 0 0 1 >> 1
  
  
  
  0    0     0   0   0   0  0  0  0 0 0 1 1 >> 3 >> current
  0    0     0   0   0   0  0  0  0 1 1 0 0 >>12 : current<<2 + 1  : 13
  
  0    0     0   0   0   0  0  0  0 1 1 0 0 >> 12>> number
  0    0     0   0   0   0  0  0  0 0 1 1 0 >>  6>> current
  0    0     0   0   0   0  0  0  0 0 0 0 1 >> 1
  0    0     0   0   0   0  0  0  0 0 0 0 0 >> 0
  
  
  0    0     0   0   0   0  0  0  0 0 1 1 0 >>  6>> number
  0    0     0   0   0   0  0  0  0 0 0 0 1 >> 1
  0    0     0   0   0   0  0  0  0 0 0 0 0 >> 0
  0    0     0   0   0   0  0  0  0 0 0 1 1 >> 3>> current  
  0    0     0   0   0   0  0  0  0 0 0 1 1 >> 3>> number
  0    0     0   0   0   0  0  0  0 0 0 0 1 >> 1
  0    0     0   0   0   0  0  0  0 0 0 0 1 >> 1
  0    0     0   0   0   0  0  0  0 0 0 0 1 >> 1>> current + 
  0    0     0   0   0   0  0  0  0 0 1 0 0 >> 4
  
  
'''