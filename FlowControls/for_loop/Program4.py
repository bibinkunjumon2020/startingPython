#Prime number

number=int(input("NUmber"))
flag='true'             # flag value normal is prime
if(number==0 or number==1):
    print("Number is neither prime nor composite")
else:
    for i in range(2,number-1):
        if(number%i ==0):
            flag='false'   #flag value not prime
            print("Number is not prime")
            break
    if(flag=='true'):
        print("Number is prime")

