
"""
Opening file named customer.
counting the nationalities count...ex//: Indians 6 people


"""
f=open("/Users/bibinkunjumon/Documents/customer.txt")
myDict={}
for i in f:
    data=i.rstrip("\n").split(",")
    nation=data[-1]
    if nation not in myDict:  # Dictionary used here
        myDict[nation]=1
    else:
        myDict[nation]+=1
print(myDict)