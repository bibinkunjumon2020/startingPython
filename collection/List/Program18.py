
#No matter what happens for loop continues its looping


for x in range(2,11,3):
    print(x,end=" ")
    if x==3:
        print("im in break")
        break
    else:
        x=x-1
        print("x=",x)
#else:
  #  print("error")

