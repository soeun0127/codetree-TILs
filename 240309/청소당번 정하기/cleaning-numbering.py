cntClass = 0
cntHall = 0
cntToilet = 0

date = int(input())

for i in range(date+1):
    if i % 12 == 0 and i != 0:
        cntToilet += 1
    elif i % 3 == 0 and i != 0:
        cntHall += 1
    elif i % 2 == 0 and i != 0:
        cntClass += 1

print(cntClass, cntHall, cntToilet)