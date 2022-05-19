"""
6. Write a Python program to count the number of even and odd numbers from a series of numbers. Go to the editor Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4

"""

numberSet=[]
count=int(input("How many numbers  "))
print("Enter your numbers .....\n")
for i in range(0,count):
    num=int(input())
    numberSet.append(num)
print("Your entered numbers are:......\n",numberSet)

evenCount=0
oddCount=0
for element in numberSet:
    if(element%2==0):
        evenCount+=1
    else:
        oddCount+=1
print("Number of even Numbers : ",evenCount)
print("Number of odd Numbers : ",oddCount)
