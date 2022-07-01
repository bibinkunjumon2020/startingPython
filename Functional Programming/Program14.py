# 1,15 elements print element of square greater than 50 elements

myList=[]
for i in range (1,16):
    myList.append(i)
print(myList)

print([i for i in myList if i**2>50])