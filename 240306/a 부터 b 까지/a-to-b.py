inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

print(a, end = " ")

for i in range(20):
    if a % 2 == 0:
        a += 3
    else:
        a *= 2
    
    if a > b:
        break 
    print(a, end = " ")