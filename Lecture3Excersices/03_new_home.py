flowers_type = input()
flowers_count = int(input())
budget = int(input())

price = 0

if flowers_type == "Roses":
    price = 5
    if flowers_count > 80:
        price *= 0.9

elif flowers_type == "Dahlias":
    price = 3.8
    if flowers_count > 90:
        price *= 0.85

elif flowers_type == "Tulips":
    price = 2.8
    if flowers_count > 80:
        price *= 0.85

elif flowers_type == "Narcissus":
    price = 3
    if flowers_count < 120:
        price *= 1.15

elif flowers_type == "Gladiolus":
    price = 2.5
    if flowers_count < 80:
        price *= 1.2

total_price = price * flowers_count

if total_price <= budget:
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {budget - total_price:.2f} leva left.")

else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")
