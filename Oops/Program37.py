#checking the characters in rule string in given string.

import re
count=0
rule="[abc]"  #rules are given in [] ,

rule2="[^abc]"  # checking except abc in given string
string_sour="abc @bibin lop"
match=re.finditer(rule,string_sour)
rule3="[a-z]"
rule4="[A-Za-z]"
rule5="[0-9]"
rule6="[ ]"
for i in match:
    print(i)
    count+=1
    print(i.start(),i.end(),i.group())
print(count)

match=re.finditer(rule2,string_sour)
count=0
for i in match:
    print(i)
    count+=1
    print(i.start(),i.end(),i.group())
print(count)