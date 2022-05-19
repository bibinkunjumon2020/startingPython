#Calculator

print(" #1.Addition \n #2.Substraction \n #3.Multiplication \n #4.Division")
choice=int(input("What's Your Choice  "))
num1=int(input("First Number  "))
num2=int(input("Second Number  "))

def Addition(num1,num2):
    return num1+num2
def Substraction(num1,num2):
    return num1-num2
def Multiply(num1,num2):
    return num1*num2
def Division(num1,num2):
    return num1/num2

if(choice==1):
    print("Sum = ",Addition(num1,num2))
elif(choice==2):
    print("Difference = ",Substraction(num1,num2))
elif(choice==3):
    print("Multiplication = ",Multiply(num1,num2))
elif(choice==4):
    print("Division = ",Division(num1,num2))
else:
    print("Improper input")