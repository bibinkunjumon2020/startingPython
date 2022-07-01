#map & filter

#map function used to apply same operation to each element in a list.

#lst=[1,2,3] --> f(x) =[1,4,9] squaring each value

#filter only for seleting certain nmbers in a list
#lst=[1,2,3,4] --->f(x)=[2,4]  selecting only even numbers

#syntax
#variable=list(map(arg1,arg2))
#variable=list(filter(arg1,arg2))

#arg1=function
#arg2=list name


lst=[1,2,3,4,5]

#method 1
def square(num):return num**2
data=list(map(square,lst))
print(data)


#method 2

def square(num):return num**2
print(list(map(square,lst)))


#method 3

print(list(map(lambda num:num**2,lst)))

