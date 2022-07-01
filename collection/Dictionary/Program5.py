dic={"roll":23,"name":'binay',"age":26,"dep":"bigdata","marks":45}

dic["marks"]+=20  # adding or sub values directly from dic
print(dic)

dic["total"]=1220  # simply add a new key value pair

print(dic)

del dic["dep"]    # deleting an element from dictionary
print(dic)


print("name" in dic)   #True  can be used in if clause

print("name" not in dic)  # False can be used in if clause