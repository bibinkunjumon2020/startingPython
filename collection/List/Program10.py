#Eliminating duplicates from a list

mylist=[10,10,20,20,30,30,40,50,60,100,80,80,90]
newlist=[]

for element in mylist:
    flag=0
    for new_element in newlist:
        if(element==new_element):
            flag=1
    if(flag==0):
        newlist.append(element)
print(newlist)

# Another method of doing the same program

mylist=[10,10,20,20,30,30,40,50,60,100,80,80,90]
newlist=[]
for i in mylist:
    if i not in newlist:
        newlist.append(i)
print(newlist)