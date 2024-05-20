men = int(input())
women = int(input())
tables = int(input())
booked_tables = 0

for man in range(1, men + 1):
    if booked_tables >= tables:
        break
    for woman in range(1, women + 1):
        if booked_tables >= tables:
            break
        print(f"({man} <-> {woman})", end=" ")
        booked_tables += 1