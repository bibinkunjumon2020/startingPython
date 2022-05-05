subject1=int(input("ENter Mark"))
subject2=int(input("ENter Mark"))
subject3=int(input("ENter Mark"))
subject4=int(input("ENter Mark"))

total=subject1+subject2+subject3+subject4
print("Total Mark = ",total,"\n Grade is")

if(total>180):
    print("A+")
elif(total>=160)&(total<180):
    print("A")
elif(total>=140)&(total<160):
    print("B+")
elif(total>=120)&(total<140):
    print("B")
elif(total>=100)&(total<120):
    print("C+")
elif(total>=80)&(total<100):
    print("C")
else:
    print("Failed")