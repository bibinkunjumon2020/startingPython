#kwargs  : key word arguments

#  **args

def printVal(**kwargs):   # Here dictionary is the output
    print(kwargs)
    print(type(kwargs))

printVal(id=101,name="bibin",pos="Engineer")