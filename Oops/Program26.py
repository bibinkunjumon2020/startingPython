"""
Finding person name from a list with maximum mark and printing that detail

"""


lst=[["bibin",34],["arun",467],["hel",100],["huwai",560],["Venom",120]]

newdict={}  # An empty dictionary for inserting values in key value order
for element in lst:
    newdict[element[1]]=element[0]  # Making marks as key and values are names
#print(newdict)
print(".....The person with max mark is ....")
print(newdict[max(newdict)],"and he scored --- ",max(newdict))  # Finding max key and using it to find the value