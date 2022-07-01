# Making a new dictionary with list of items and list

employee=['vinay','anu']

dic1={"designation":"bigdata","salary":1000}
dic4={"new":"hai","old":"bye"}
dic3={}
for element in employee:
    dic2={element:dic1}
    dic3.update(dic2)
print(dic3)
#fromkeys : it returns wiith specified keys with specified values

"""
dictionary with in dictionary. Key is from list and values are another Key-Value Pair
"""
newdict=dict.fromkeys(employee,dic1)
print(newdict)



print(newdict["anu"])

"""
List values are keys of new dictionary and dict keys are values of new dictionary

"""
print("********************")
myDict=dict(zip(employee,dic1))
print(myDict)

"""
list values are --keys of new dictionary-- and dictionary values are Values of new dictionary
"""
print("*******")
myDict2=dict(zip(employee,dic1.values()))
print(myDict2)

"""
Key of first dict is key and keys of 2nd dictionary is values
"""
myDict3=dict(zip(dic4,dic1))
print(myDict3)