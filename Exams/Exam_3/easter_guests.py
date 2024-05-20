from math import ceil

guests = int(input())
budget = int(input())

easter_bread_price = ceil(guests / 3) * 4
eggs_price = guests * 2 * 0.45

total = eggs_price + easter_bread_price

if total <= budget:
    print(f"Lyubo bought {ceil(guests / 3)} Easter bread and {guests * 2} eggs.")
    print(f"He has {budget - total:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {total - budget:.2f} lv. more.")