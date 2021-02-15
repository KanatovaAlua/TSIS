x= list(map(int,input().split()))
mini=1000
for i in range(len(x)):
    if x[i]>0 and x[i]<mini:
        mini=x[i]
print(mini)             