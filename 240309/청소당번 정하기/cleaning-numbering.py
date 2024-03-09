cntClass = 0
cntHall = 0
cntToilet = 0

date = int(input())

for i in range(1,date):
    if i % 12 == 0:
        cntToilet += 1
    elif i % 3 == 0:
        cntHall += 1
    elif i % 2 == 0:
        cntClass += 1

print(cntClass, cntHall, cntToilet)