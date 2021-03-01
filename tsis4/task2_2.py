#Re.split()
'''
import re

ans=re.split(r",|\.", input())

for i in ans:
    print(i)
'''
regex_pattern = r",|\."

import re
print("\n".join(re.split(regex_pattern, input())))