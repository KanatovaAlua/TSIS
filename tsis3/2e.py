x,y=map(int,input().split())
a=[]
b=[]
for i in range(x):
    a.append(int(input()))

for i in range(y):
    b.append(int(input()))

a=set(a)
b=set(b)

q=sorted(a.intersection(b))
w=sorted(a.difference(q))
e=sorted(b.difference(q))

print(len(q))
print(*q)
print(len(w))
print(*w)
print(len(e))
print(*e)
