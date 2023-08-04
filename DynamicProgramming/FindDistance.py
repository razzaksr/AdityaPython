def determineDistance(para1,para2):
     #6, 7
    lenPara1,lenPara2=len(para1),len(para2)
            # rows count
            # 7,6
    steps=[[0 for _ in range(lenPara2+1)] for _ in range(lenPara1+1)]
    
    for traverser in range(lenPara1+1):
        for pointer in range(lenPara2+1):
            if traverser==0:
                #      0         0       = 0
                steps[traverser][pointer]=pointer;# 0,0 >>0, 0,1>>1, 0,2>>2
            elif pointer==0:
                steps[traverser][pointer]=traverser
            elif para1[traverser-1]==para2[pointer-1]:
                steps[traverser][pointer]=steps[traverser-1][pointer-1]
            else:
                # steps[traverser-1][pointer]# deletion
                # steps[traverser][pointer-1]# insertion
                # steps[traverser-1][pointer-1]# replace
                steps[traverser][pointer]=1+min(steps[traverser-1][pointer],steps[traverser][pointer-1],steps[traverser-1][pointer-1])
    return steps[lenPara1][lenPara2]

myString1="madam"
myString2="mam"
required=determineDistance(myString1,myString2)
print(required,"steps required to change",myString1,"to",myString2)