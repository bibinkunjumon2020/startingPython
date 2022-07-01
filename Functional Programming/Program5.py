

#list comprehension

myList=[]
for i in range(1,101):
    myList.append(i)
print(myList)


lst=[i for i in range(1,101)]
print(lst)


lst1=[i for i in range(1,76,4)]
print(lst1)

lst2=["even" for i in range(1,101) if i%2==0]
print(lst2)

lst3=[(i,"even") for i in range(1,101) if i%2==0]
print(lst3)

