# Largest among 3 numbers

num1=int(input("Number Pls"))
num2=int(input("Number Pls"))
num3=int(input("Number Pls"))
"""
if(num1>num2):
    if(num1>num3):
        print("I am Big ",num1)
elif(num2>num3):
    print("Big",num2)
else:
    print("Big",num3)"""

if(num1>num2)&(num1>num3):
    print("NUmber 1 is largest",num1)
elif(num2>num1)&(num2>num3):
    print("NUmber2 is large",num2)
else:
    print("NUmber 3 is largest",num3)