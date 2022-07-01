#Reading numbers from file,Adding into list,and Printing sum
myList=[]
content=open("sample1")
for element in content:
    myList.append(int(element.rstrip("\n")))
print(myList)
print(sum(myList))
#Here \n is added to list elements. so rstrip used to remove that