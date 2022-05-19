# Pyhon program to print prime number between 0 to 100

for number in range(0,101):
    flag = 1
    if(number==0 or number==1):
        continue
    for check in range(2,(number//2)+1):
        if(number%check==0):
            flag=0
            break
    if(flag==1):
        print(number)

