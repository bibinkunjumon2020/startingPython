
# Removing special characters from a file and counting the words

f=open("contents")
splChar="!@#$%^&*()_+?:;.,-=/"
myList=[]
for i in f:
    data=i.rstrip("\n")  # dividing a string by line..
    string1=""
    for j in data:
        if j not in splChar:
            string1+=j
    myList.append(string1)
print(myList)   # List contains all the words and spaces too but no special characters
wordCount=0
for i in myList:
    data=i.rsplit()   # List of words as a list
    print(data)
    for j in data:
        wordCount+=1
print(wordCount)


