
#Creating a list and appending values up to 100
myList=[]
for i in range(1,101):
    myList.append(i)
print(myList)

#Inserting even numbers into new list

newList=[]
for i in myList:
    if(i%2==0):
        newList.append(i)
print(newList)