myList=[
    [100,'bibin','k',28,'python',1000],
    [101,'varun','a',26,'big data',1500],
    [102,'richu','b',30,'html',2000],
    [103,'veego','r',18,'oyur',3000]
]



for element in myList:
    if(element[3]>25):
        print(element[1:6])