#Parent class varibales and methods inherited in another class



class A:  #parent/base/super class
    def printa(self,num1):
        self.num1=num1
        print("Inside class A",self.num1)


class B(A):   #Child/subclass/derived
    def printb(self,num2):
        self.num2=num2
        print("Inside class B",self.num2,self.num1)


b=B()
b.printa(30)
b.printb(23)


