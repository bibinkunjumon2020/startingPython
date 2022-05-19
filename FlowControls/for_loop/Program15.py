# Lower limit , Upper limit print prime number in between

lower=int(input("Lower Limit Pls..."))
upper=int(input("Upper Limit Pls..."))
for i in range(lower,upper+1):
    flag=1
    for j in range(2,(i//2)+1):
        if(i%j ==0):
            flag=0

    if(flag == 1):
        print(i)

