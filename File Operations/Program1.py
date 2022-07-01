#File Operations - Read (r) Write (w) Append(a)
#File Reference :    fileName=open(path,mode)


#read operation

content=open("/Users/bibinkunjumon/PycharmProjects/startingPython/File Operations/sample1")
print(content.read())
content.close()

#Since both files are in same directory
content=open("sample1")
#print(content.read())
print(".............")
for i in content:
    print(i)
content.close()