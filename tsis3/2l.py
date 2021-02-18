x=int(input())
d=dict()
for i in range(x):
    a,b=map(str,input().split())
    d[a]=b
    d[b]=a
q=str(input())
print(d[q])