lst=[1,2,3,4]

def even(num):return num%2==0

date=list(filter(even,lst))
print(date)


date=list(filter(lambda num:num%2==0,lst))
print(date)


print(list(filter(lambda num:num%2==0,lst)))
