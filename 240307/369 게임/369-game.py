n = int(input())
i = 1

while i <= n:
    if i < 10:
        if i % 3 == 0:
            print(0, end = " ")
        elif (i%10) % 3 == 0:
            print(0, end = " ")
        else:
            print(i, end = " ")
        i += 1
    elif i % 10 == 0 and i % 3 != 0:
        print(i)
    else:
        if i % 3 == 0:
            print(0, end = " ")
        elif (i%10) % 3 == 0:
            print(0, end = " ")
        elif (i//10) % 3 == 0:
            print(0, end = " ")
        else:
            print(i, end = " ")
        i += 1