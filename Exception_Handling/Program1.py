num1=int(input("Number 1"))
num2=int(input("Number 2"))

try:
    print(num1/num2)
except:
    print("Division error")
finally:
    print("I always work..whether exception there or not..i work")