#Find Cube of a number

#Type 1
def Cube():
    num=int(input("Your NUmber Pls..."))
    result=num**3
    print("Type 1 Result = ",result)
Cube()

#Type 2

def Cube_1(num):
    result=num**3
    print("Type 2 Result = ",result)

num=int(input("Your Number"))
Cube_1(num)

#Type 3

def Cube_2(num):
    return num**3

print("Type 3 Result = ",Cube_2(int(input("Ypur Number"))))