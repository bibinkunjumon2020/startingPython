st={23,45,67,8,9,9,9,9,}
st1={}

#to avoid duplicates
lst=list(st)
print(lst)
st10=set(lst)
print(st10)

#-------------

print(type(st)) #class -> set

print(type(st1)) # Empty set is a dictionary -- class->dict

print(st)

print(len(st)) # It avoid duplicates

print(max(st))  # printing big value

print(min(st))  # Print small value

print(sum(st))  # It avoid duplicates..

st.add(100)  # Only one element is added
print(st)

st.update([105,56,78])  # adding multiple values but not in order
print(st)

st2={1,2,3,4,5}
st3={6,7,8,1,2}

st4=st2.union(st3)  # Both set elements
print(st4)

st5=st2.intersection(st3)  # Only common one
print(st5)

st6=st2.difference(st3) # st2-st3
print(st6)

st7=st3.difference(st2) #st3-st2
print(st7)

#-------

st7.remove(6)  # if the element not present then error
print(st7)
#st7.remove(6)  # Error

st7.discard(6) #if element present remove..if not no issue
print(st7)




