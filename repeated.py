def findDuplicates(paragraph):
    para=paragraph.split(" ")
    for hold in range(len(para)):
        for compare in range(hold+1, len(para)):
            if para[hold]==para[compare]:
                print(para[hold],"repeats @ ",(hold+1), (compare+1))

def findDups(paragraph):
    para=paragraph.split(" ")
    para.sort()
    for index in range(len(para)-1):
        if para[index]==para[index+1]:
            print(para[index],"repeats")
        index+=1
        
def findPairs(paragraph):
    para=paragraph.split(" ")
    for index in range(len(para)):
        if para.count(para[index])>=2:
            print(para[index],"repeats")
        index+=1

#findPairs("Python is suitable for performing testing machine learning developing for web application even desktop application")
#findDups("Python is suitable for performing testing machine learning developing for web application even desktop application")
findDuplicates("Python is suitable for performing testing machine learning developing for web application even desktop application")