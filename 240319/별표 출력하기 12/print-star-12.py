n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0:
            print("*", end = " ")
        elif j % 2 != 0:
            if i <= j:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        else:
            print(" ", end = " ")
    print()