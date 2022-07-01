#Polymorphism->method overloading,method overriding

class Add:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2

class Add1(Add):
    def sum(self,num1,num2,num3):  #method overloading happening
        self.num1=num1
        self.num2=num2
        self.num3=num3
        print(self.num1+self.num2+self.num3)


ob=Add1()
ob.sum(2,3,4)