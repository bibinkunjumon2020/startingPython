"""

4. Print a pattern like
        1
        23
        456
        7 8 9 10
        11 12 13 14 15
"""
display=1
for row in range(1,6):
    for column in range(0,row):
        print(display,end=" ")
        display+=1
    print()