def dynamicKnapsack(weights, values, knapCapacity):
    lengthWeights=len(weights) # 4
    # nested list: maxPossy[0]=[5,3,3,5,2], maxPossy[1]=[9,1,32,34,43]
    # maxPossy[0][1] >> 3, maxPossy[1][4]>> 43
    maxPossy=[[0 for _ in range(knapCapacity+1)] for _ in range(lengthWeights+1)]
    
    # 1 to 4
    for current in range(1,lengthWeights+1):
        # 1 to 5
        for wt in range(1, knapCapacity+1):
            # 2<=2
            if weights[current-1]<=wt:
                # maxPossy[1][2]=max(0,4+maxPossy[0][0])
                maxPossy[current][wt]=max(maxPossy[current-1][wt], 
                                          values[current-1]+maxPossy[current-1][wt-weights[current-1]])
            else:
                # maxPossy[1][1]=0
                maxPossy[current][wt]=maxPossy[current-1][wt]
                
    # backtracking
    benefitFruits=[]
    cap=knapCapacity
    for current in range(lengthWeights,0,-1):
        if maxPossy[current][cap]!= maxPossy[current-1][cap]:
            benefitFruits.append(current-1)
            cap-=weights[current-1]
            
    benefitFruits.reverse()
    return maxPossy[lengthWeights][knapCapacity], benefitFruits
                
fruits=["Apple","Banana","Orange","Watermelon"]
weights=[2,1,3,4]
values=[4,3,5,7]
capacity=5

profit, products=dynamicKnapsack(weights,values,capacity)

print("Profit i have got",profit)
print("Fruit peroducts are ",[fruits[current] for current in products])