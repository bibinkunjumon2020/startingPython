#if even print square if odd print the number

print([i**2 if i%2==0 else i for i in range(1,51)])

# To print number and result

print([(i,i**2) if i%2==0 else (i,i) for i in range(1,51)])

