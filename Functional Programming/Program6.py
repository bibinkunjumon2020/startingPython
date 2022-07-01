
#list comprehension

#{print1 if condition1 else print2 'range']

#{print1 if condition1 else print2 if condition2 else print 'range']


# 1, 50 if even print square if odd print cube


lst=[i**2 if i%2==0 else i**3 for i in range(1,51)]
print(lst)

print([i**2 if i%2==0 else i**3 for i in range(1,51)])
