
# Method overrriding
class A:
    def printa(self):
        print("Method 1")
    def printa(self):
        print("Method 2")
ob=A()
ob.printa()