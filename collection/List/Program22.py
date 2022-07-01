myList=[
    [100,'bibin','k',28,'python',1000],
    [101,'varun','a',26,'big data',1500],
    [102,'richu','b',30,'big data',2000],
    [103,'veego','r',18,'big data',3000]
]

#printing values of bigdata profession persons
for element in myList:
    if(element[3] > 25 and element[5]>1750 ):
        print(element[1:6])
