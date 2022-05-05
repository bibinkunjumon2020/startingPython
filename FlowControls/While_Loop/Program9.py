#Print sum of odd and even numbers


lower=int(input("Lower LImit"))
upper=int(input("Upper LImit"))

evenSum=0
oddSum=0
while(lower<=upper):
    if(lower%2==0):
        evenSum+=lower
    else:
        oddSum+=lower
    lower+=1
print("Even Sum = ",evenSum,"\n Odd Sum = ",oddSum)
