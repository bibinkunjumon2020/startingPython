lower=int(input("Lowe Limit"))
upper=int(input("Upper Limit"))
evenSum=0
oddSum=0
for i in range (lower,upper+1):
    if(i%2==0):
        evenSum+=i
    else:
        oddSum+=i
print("Even Sum = ",evenSum)
print("Odd Sum = ",oddSum)