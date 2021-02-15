x=list(map(int,input().split()))
g=[]
for i in x:
    if i!=0:
        g.append(i)

for i in range(len(x)-len(g)):
    g.append(0) 
for i in g:
    print(i, end=" ")
