n = int(input())

for i in range(n*2):
    if i % 2 != 0 and i != 0 and i != n*2-1:
        for _ in range(n - (i - 1) // 2):
            print("*", end = " ")
        print()
    elif i % 2 == 0 and i != n and i != n*2-1:
        for _ in range(1 + (i // 2)):
            print("*", end = " ")
        print()
    else:
        print("*")