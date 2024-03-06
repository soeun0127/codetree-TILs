a, b = tuple(map(float, input().split()))

i = 0
c = 0
c = a / b
print(c, end = "")
while i < 19:
    a = int(a)
    b = int(b)
    d = a // b
    print(d, end = "")
    i += 1