
# Regular Expression - checking the patterns in string by importing package called re

import re
string_start="aababababbbbbaa ba b"
check='ab'
count=0
match=re.finditer(check,string_start)
for i in match:
    count+=1
    print(i.start(),i.end(),i.group(),i.span())
print(count)