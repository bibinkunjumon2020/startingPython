# Method Overriding

class A:
    def printa(self):
        print("Inside clas A")
class B:
    def printa(self):
        print("Inside class B")
    def printa(self):
        print("go man")
    def printa(self):
            print("paka paka")
ob=B()
ob.printa()