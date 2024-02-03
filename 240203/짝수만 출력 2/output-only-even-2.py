a, b = tuple(map(int, input().split()))

i = b
if a % 2 == 0:
    re = a
else:
    re = a - 1

while re >= i:
    print(re, end = " ")
    re -= 2