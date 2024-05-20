groups = int(input())
total = 0
musala = 0
monblan = 0
kilimangaro = 0
k2 = 0
everest = 0

for i in range(groups):
    people = int(input())

    if people >= 41:
        everest += people
    elif people >= 26:
        k2 += people
    elif people >= 13:
        kilimangaro += people
    elif people >= 6:
        monblan += people
    else:
        musala += people
    total += people

print(f"{musala / total * 100:.2f}%")
print(f"{monblan / total * 100:.2f}%")
print(f"{kilimangaro / total * 100:.2f}%")
print(f"{k2 / total * 100:.2f}%")
print(f"{everest / total * 100:.2f}%")

