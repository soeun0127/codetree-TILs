n = int(input())
cnt = 0

for i in range(1, 100):
    if i % 4 == 0:
        if i % 400 != 0:
            cnt += 1

print(cnt)