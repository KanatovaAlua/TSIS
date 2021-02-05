def numIdenticalPairs(nums):
    s=0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]==nums[j] and i<j:
                s+=1
    return s

h=[]
for i in range(4):
    g=int(input())
    h.append(g)
j=numIdenticalPairs(h)
print(j)