#Reverse

"""number=int(input("Number"))
result=""
while(number//10!=0):
    result= result+ str(number%10 )
    number=number//10
result= result+str(number%10)
print(result)"""

number=int(input("Number"))
result=0
while(number!=0):
    result= result*10 + number%10
    number=number//10

print(result)