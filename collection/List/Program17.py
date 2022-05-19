myList=[4,3,2,1]

pair=int(input("number"))
for element in myList:
    for element1 in myList:
        if(element+element1==pair):
            print("[",element,",",element1,"]")
