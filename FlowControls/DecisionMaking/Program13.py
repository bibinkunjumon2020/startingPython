#Second Largest
i=1
num1=int(input("Number 1"))
num2=int(input("Number 2"))
num3=int(input("Number 3"))

if (num1>num2 and num1>num3 and num2>num3):
    print("Seconnd Biggest : ",num2)
elif(num1>num2 and num1>num3 and num2<num3):
    print("Seconnd Biggest : ", num3)
elif (num2>num1 and num2>num3 and num1>num3):
    print("Seconnd Biggest : ",num1)
elif(num2>num1 and num2>num3 and num1<num3):
    print("Seconnd Biggest : ", num3)
elif (num3>num1 and num3>num2 and num1>num2):
    print("Seconnd Biggest : ",num1)
elif(num3>num1 and num3>num2 and num1<num2):
    print("Second Biggest : ", num2)
else:
    print("Error")