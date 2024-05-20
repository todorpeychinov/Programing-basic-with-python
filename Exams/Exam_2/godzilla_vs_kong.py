budget = float(input())
statists_count = int(input())
statists_clothes_price = float(input())

decor = 0.1 * budget
statists_clothes = statists_count * statists_clothes_price

if statists_count > 150:
    statists_clothes *= 0.9

total_price = decor + statists_clothes

if total_price > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_price - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_price:.2f} leva left.")
