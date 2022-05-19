
mylist=[5,10.5,"bibin"] # definition
print(mylist)

print(mylist[2])  # printing particular value

#index range from 0 to n-1
mylist.append(90)  # Can insert new value
print(mylist)

mylist.append(90) # duplicates allowed and size of list is not limited
print(mylist)

mylist[1]='hello' # list is mutable
print(mylist)

#mylist.clear()  # clearing list values
print(mylist)

print(len(mylist)) # length of list function

mylist.reverse()  # Reversing the whole list
print(mylist)

mylist.insert(3,56) #inserted 56 value into index 3. the eralier value there shifted to next index
print(mylist)

newllist=[10,15,20,25,30,40,'bibin','hai']
for i in newllist:
    print(i)

for i in range(len(newllist)):
    print(newllist[i])