#printing word count
content=open("sample2")
wordCount=0
mylist=[]

for element in content:
    data=element.rstrip("\n").rsplit(" ")
    for i in data:
        mylist.append(data)
print(mylist)
for i in mylist:
    wordCount+=1
print(wordCount)

