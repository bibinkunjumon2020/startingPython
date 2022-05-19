#Binary Search
myList=[7,4,3,1,2]
#Sort the given list
myList.sort()
print(myList)
key=int(input("Search Key"))   #to be searched
low=0           #setting lower value
upper=len(myList)-1
flag=0
for i in range(low,upper):
    mid=(low+upper)//2  # always put bracket
    if(key==myList[mid]):
        flag=1
        break
    elif(key<myList[mid]):
        upper=mid-1
    elif (key>myList[mid]):
        low=mid+1

if(flag>0):
    print("given number  in list")
else:
    print("Not found")