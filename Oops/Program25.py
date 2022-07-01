class Customer:
    def __init__(self,id,fname,lname,age,prof,loc):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.prof=prof
        self.loc=loc
    def printVal(self):
        print(self.id,self.fname,self.lname,self.age,self.prof,self.loc)

f=open("/Users/bibinkunjumon/Documents/customer.txt")
for element in f:
    data=element.rstrip("\n").rsplit(",")
    try:
        obj=Customer(data[0],data[1],data[2],data[3],data[4],data[5])
    except Exception as e:
        print(e)
    obj.printVal()
    lst=[obj.id,obj.fname,obj.lname,obj.age,obj.prof,obj.loc]
    print(lst)
