#Prime number

number=int(input("NUmber"))
for i in range(2,number-1):
    if(number%i ==0):
        print("NUmber is not prime")
        break
    else:
        print("NUmber is prime")
