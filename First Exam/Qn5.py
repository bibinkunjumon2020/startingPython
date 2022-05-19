"""
5. Print a pattern like
        12345
        22345
        33345
        44445
        55555
"""

for row in range(1,6):
    for column in range(0,5):
        print(row+column,end="")
    print()
