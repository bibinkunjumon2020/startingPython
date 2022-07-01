
"""
Opening file named customer.
counting the profession persons count...ex//: Engineer 6 people Teacher  3 people


"""
f=open("/Users/bibinkunjumon/Documents/customer.txt")
myDict={}
for i in f:
    data=i.rstrip("\n").split(",")
    nation=data[4]
    if nation not in myDict:    # Dictionary used here
        myDict[nation]=1
    else:
        myDict[nation]+=1
print(myDict)