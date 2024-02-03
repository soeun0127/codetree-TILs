sex = int(input())
age = int(input())

if sex == 0:
    if age >= 20:
        print("MAN")
    else:
        print("BOY")
else:
    if age >= 20:
        print("WOMAN")
    else:
        print("GIRL")