count = int(input())
type = input()
delivery = input()
price_per_one = 0

if count < 10:
    print("Invalid order")
    exit()

if type == "90X130":
    price = 110
    if count > 60:
        price *= 0.92
    elif count > 30:
        price *= 0.95
elif type == "100X150":
    price = 140
    if count > 80:
        price *= 0.9
    elif count > 40:
        price *= 0.94
elif type == "130X180":
    price = 190
    if count > 50:
        price *= 0.88
    elif count > 20:
        price *= 0.93
else:
    price = 250
    if count > 50:
        price *= 0.86
    elif count > 25:
        price *= 0.91

total = count * price

if delivery == "With delivery":
    total += 60

if count > 99:
    total *= 0.96

print(f"{total:.2f} BGN")
