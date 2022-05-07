#Prime number

number=int(input("NUmber"))
flag='true'             # flag value normal is prime
for i in range(2,number-1):
    if(number%i ==0):
        flag='false'   #flag value not prime
        print("NUmber is not prime")
        break
if(flag=='true'):
    print("Number is prime")

