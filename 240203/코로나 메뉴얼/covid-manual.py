inp1 = input()
inp2 = input()
inp3 = input()

arr1 = inp1.split()
arr2 = inp2.split()
arr3 = inp3.split()

c1, t1 = arr1[0], int(arr1[1])
c2, t2 = arr2[0], int(arr2[1])
c3, t3 = arr3[0], int(arr3[1])

if c1 == 'Y' and t1 >= 37:
    if (c2 == 'Y' and t2 >= 37) or (c3 == 'Y' and t3 >= 37):
        print("E")
    else:
        print("N")
else:
    if(c2 == 'Y' and t2 >= 37) and (c3 == 'Y' and t3 >= 37):
        print("E")
    else:
        print("N")
"""
if c1 == 'Y':
    if c2 == 'Y' and t2 >= 37: #2A
        if t1 >= 37: #1A
            print("E")
        elif t3 >= 37 and c3 == 'Y': #3A
            print("E")
        else:
            print("N")
    elif t3 >= 37 and c3 == 'Y': #3A
        if t1 >= 37: #1A
            print("E")
        else:
            print("N")
    else:
        print("N")
elif c2 == 'Y' and c3 == 'Y':
    if t2 >= 37 and t3 >= 37:
        print("E")
    else:
        print("N")
else:
    print("N")
        """