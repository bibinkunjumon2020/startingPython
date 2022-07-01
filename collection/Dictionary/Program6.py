myDict={"name":"Bibin","age":23,"prof":"Engineer","salary":90000}
#1.
print(myDict["prof"])
#2.
if("company" not in myDict):
    myDict["company"]="luminar"
print(myDict)
#3. Adding 5000 to salary
myDict["salary"]+=5000
print(myDict)
#4. Printing key value pairs
for element in myDict:
    print(element,myDict[element])

#5.  Updating Key
myDict["fname"]=myDict["name"]
del myDict["name"]
print(myDict)

#6.Deleting present key and adding new key in a line --- pop

myDict["fage"]=myDict.pop("age")
print(myDict)


#7.Changing All keys without changing values
'''
newDict is a dictionary/zip takes 2 args -> Both are lists -> first list is used as keys & 2nd list is used as values.
'''

ini_list = ['a', 'b', 'c', 'd','e']
newDict= dict(zip(ini_list, list(myDict.values())))
print(newDict)

print(myDict.values()) # To print only values without key in a dictionary

key_list=["name","phn_no","age"]
value_list=["Bibin",8547737607,76]
thisDict=dict(zip(key_list,value_list))
print(thisDict)