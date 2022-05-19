#Factorial
#type 1
def factorial():
    print("Type 1")
    num=int(input("Your Number"))
    result=1
    for i in range(1,num+1):
        result*=i
    print(result)

factorial() # Calling Function

#type 2
def factorial_1(num):
    print("Type 2")
    result=1
    for i in range(1,num+1):
        result*=i
    print(result)
num1=int(input("Your Number"))

factorial_1(num1)

#type 3

def factorial_2(num):
    print("Type 3")
    result=1
    for i in range(1,num+1):
        result*=i
    return result
num2=int(input("Your Number"))
result=factorial_2(num2)
print(result)