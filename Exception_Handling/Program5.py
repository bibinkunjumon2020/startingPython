

age=int(input("Your Age"))

if age>=18:
    print("eligibile")
else:
    raise Exception("Enter proper age idiot")  # Raising an exception when wrong input
