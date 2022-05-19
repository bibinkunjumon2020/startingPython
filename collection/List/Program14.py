#Linear Search

myList=[15,5,12,19,9,4,45,20,8,90,31]

key=int(input("Your number"))
flag=0
for element in myList:
    if (element==key):
        print("Elelemnt Found")
        flag=1
        break
if(flag==0):
    print("Element not Found")