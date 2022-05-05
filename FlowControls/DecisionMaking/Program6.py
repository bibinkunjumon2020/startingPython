"""
Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :

        Cost price (in Rs)                                       Tax
        > 100000                                                  15 %
        > 50000 and <= 100000                          10%
        <= 50000                                                  5%

"""


bikeCost=int(input("Bike Cost"))
if(bikeCost>100000):
    print("Above 1 Lakh Tax = ",bikeCost*0.15)
else:
    if (bikeCost>50000 ):
        print(" Above 50k Tax = ",bikeCost*0.10)
    else:
        print("Less than 50 k Tax = ",bikeCost*0.05)