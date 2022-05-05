#Open , Read a file

f=open("F:\\hai.txt") #open file in default read mode
print(f.read())
f.close()



#open and write a file (Always rewrite)

a=open("F:\\first.txt","w")  # Created a new file in write mode
a.write(input("Enter data for the file")) # take input from conole
a.close()
b=open("F:\\first.txt") #Open specific file in write mode
print(b.read())
b.close()