
# Multiple inheritance

class A:
    def printa(self):
        print("Inside A")
class B:
    def printb(self):
        print("Inside B")
class C(A,B):
    def printc(self):
        print("Inside C")
    

ob=C()
ob.printc()
ob.printb()
ob.printa()