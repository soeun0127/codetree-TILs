"""n = int(input())
cnt = 0
for i in range(n):
    if i % 2 == 0:
        for j in range(1, n+1):
            if j == 1 and i != 0:
                cnt += n
            else:
                cnt += 1
            print(cnt, end = " ")
        print()
    else:
        for j in range(1, n+1):
            if j == 1:
                cnt += n
            else:
                cnt += -1
            print(cnt, end = " ")
        print()
"""

n = int(input())

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print((i * n) + j + 1, end = " ")
        else:
            print((i * n) + n - j, end = " ")
    print()