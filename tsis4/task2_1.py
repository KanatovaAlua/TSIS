#Detect Floating Point Number
import re

x=int(input())

list1=[]

for _ in range(x):
    list1.append(bool(re.match(r'^[+-]?\d*?\.{1}\d+$', input())))

for i in list1:
    print(i)