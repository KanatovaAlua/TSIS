#Group(), Groups() & Groupdict()
import re
print(re.search(r"([A-Za-z0-9])\1+", input()).group(1))