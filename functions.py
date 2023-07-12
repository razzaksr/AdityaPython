# normal function

gamma,alpha=20,98

# & | ^ >> <<

'''
1024 512 256 128 64 32 16 8 4 2 1
   0   0   0   0  0  0  1 0 1 0 0   >> 20>> gamma
   0   0   0   0  1  1  0 0 0 1 0   >> 98>> alpha
   0   0   0   0  1  1  1 0 1 1 0   >>118>> gamma
   0   0   0   0  0  0  1 0 1 0 0   >> 20>> alpha
   0   0   0   0  1  1  0 0 0 1 0   >> 98>> gamma
'''

def swapByBitwise():
    global gamma
    global alpha
    gamma^=alpha
    alpha^=gamma
    gamma^=alpha
    #print("Gamma ",gamma," alpha ",alpha)
    
# print("Gamma ",gamma," alpha ",alpha)
# swapByBitwise()
# print("Gamma ",gamma," alpha ",alpha)

machineDollar=2500

# parameters:
def withdraw(requiredDollars):
    global machineDollar
    if requiredDollars%20==0:
        machineDollar-=requiredDollars;
        print(requiredDollars,"$ has successfully dispensed")
        return
    else:
        print("Invalid denomination")
        withdraw(int(input("enter the $ required....")))
        
#withdraw(int(input("enter the $ required....")))

accountAvailable=127845.5

#default arguments
def rtgsTransaction(beneficiaryName,amount=50000):
    global accountAvailable
    if amount<=accountAvailable and amount>=50000:
        accountAvailable-=amount;
        print(amount," has transferred to ",beneficiaryName)
    else:
        print("Invalid amount to transfer ",beneficiaryName)
        
rtgsTransaction("Nagaraju")
rtgsTransaction(amount=60000,beneficiaryName="Senthilnathan")
rtgsTransaction("Saravanan",10000)