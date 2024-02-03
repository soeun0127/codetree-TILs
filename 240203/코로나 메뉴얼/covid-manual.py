inp1 = input()
inp2 = input()
inp3 = input()

arr1 = inp1.split()
arr2 = inp2.split()
arr3 = inp3.split()

c1, t1 = arr1[0], int(arr1[1])
c2, t2 = arr2[0], int(arr2[1])
c3, t3 = arr3[0], int(arr3[1])

if c1 == 'Y' or c2 == 'Y':
    if c3 == 'Y':
        if t1 >= 37 or t2 >= 37:
            if t3 >= 37:
                print("E")
            else:
                print("N")
        else:
            print("N")
    else:
        print("N")
else:
    print("N")