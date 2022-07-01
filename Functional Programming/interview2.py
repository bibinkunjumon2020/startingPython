
readString=input("your string")
vowels="aeiouAEIOU"
emptyString=""
for i in readString:
       if i not in vowels:
            emptyString+=i

print(emptyString)