
# Removing special characters from a file

f=open("contents")
splChar="!@#$%^&*()_+?:;.,-=/"
myList=[]
for i in f:
    data=i.rstrip("\n")
    string1=""
    for j in data:
        if j not in splChar:
            string1+=j
    print(string1)
    myList.append(string1)
print(myList)
print(len(myList))

