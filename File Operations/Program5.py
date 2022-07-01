
f=open("/Users/bibinkunjumon/Documents/bibin.txt")

for i in f:
    data=i.rstrip("\n").split(",")

    age=int(data[4])
    if(age>=50):
        print(data[1:4])
    if(data[4]>'50' and data[-1]=='india'):
        print(data[1:5])