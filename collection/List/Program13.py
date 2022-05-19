#list sliciing printing selected areas

myList=[15,5,12,19,9,4,45,20,8,90,31]
print(myList[1:4])  # start with index 1 and print upto index 3

print(myList[:5])  # printing from 0 upto 4

print(myList[3:]) # printing frpm 3 upto end
print(myList[:])  # full list is printed


#Negative index printing from end

print(myList[-1])
print(myList[-3])
print(myList[-4:-1])  # wont print -1 index value

#  print(myList[-2,-4]) Error bcs index order is wrong

print(myList[-3:])  #-3,-2,-1
print(myList[:-4]) #upper ayondu -4 print akilla