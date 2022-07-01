#Polymorphism->method overriding

class Add1:
    def sum(self,num1,num2):
        print("inside Add1")
        self.num1=num1
        self.num2=num2
        print(self.num1 + self.num2)
class Add2(Add1):
    def sum(self,num1,num2):  #method over riding child class override parent
        print("inside Add2")
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)


ob=Add2()
ob.sum(2,3)