
dic={"roll":23,"name":"bibin"}  #definition
print(dic)
print(dic["name"])
print(dic["roll"])

dic["name"]=67  # Mutable
print(dic)  # Insertion order preserved
dic["name"]="My new name"
print(dic)