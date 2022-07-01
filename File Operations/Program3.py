#Reading numbers from file,Adding into list,and Printing sum
myList=[]
evenList=[]
oddList=[]
content=open("sample1")
for element in content:
    myList.append(int(element.rstrip("\n")))
print(myList)
print(sum(myList))
for element in myList:
    if(element % 2 == 0):
        evenList.append(element)
    else:
        oddList.append(element)
print("Even Sum = ",sum(evenList))
print("Odd Sum = ",sum(oddList))

#Here \n is added to list elements. so rstrip used to remove that