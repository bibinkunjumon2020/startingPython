"""A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
"""



totalClass=int(input("Total Classes Held"))
attendedClass=int(input("How many you attended"))
print("Percentage = ",attendedClass * 100 /totalClass)
if((attendedClass * 100 /totalClass)>=75):
    print("You can appear in Exam")
else:
    print("No Exam - Go and sit in Class first")