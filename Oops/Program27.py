#*args

def printVal(*args):   #anyname can be given after*
    print(args)  # tuple format
    print(*args) # normal
    print(args[1]) # individual arguments

printVal(12,23)