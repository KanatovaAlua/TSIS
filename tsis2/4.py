def largestAltitude(gain):
    sol=0
    maxi=0
    for i in gain:
        sol+=i
        if sol>maxi:
            maxi=sol
    return maxi
    
g=[]
for i in range(5):
    h=int(input())
    g.append(h)

j=largestAltitude(g)
print(j)