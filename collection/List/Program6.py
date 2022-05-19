myList=[]
evenList=[]
oddList=[]
for num in range(1,76):
    myList.append(num)

for element in myList:
    if(element%2==0):
        evenList.append(element)
    else:
        oddList.append(element)
print("The Original List.....\n",myList,"\n Sum= ",sum(myList))

print("The Even List is ......\n",evenList,"\nSum of Even Numbers= ",sum(evenList))

print("The Odd List is ......\n",oddList,"\nSum of Odd Numbers = ",sum(oddList))