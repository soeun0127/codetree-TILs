n = int(input())

num = 2

while num < n:
    if n % num == 0:
        print("C")
        break
    else:
        num += 1
    if n - num == 1:
        print("N")