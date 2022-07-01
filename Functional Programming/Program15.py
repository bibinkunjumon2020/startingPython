dic={"sedan":1500,"suv":2000,"pickup":2500,"minivan":1600,"semi":13600}

#weight above 2000->collect name of vehicle

myList=[i.upper() for i in dic if dic[i]>1500]
print(myList)