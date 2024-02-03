a, b, c = tuple(map(int, input().split()))

if a > b:
    if b > c:
        print(b)
    elif c > a:
        print(a)
    else:
        print(c)
else: # b > a
    if c > b:
        print(b)
    elif a > c:
        print(a)
    else:
        print(c)