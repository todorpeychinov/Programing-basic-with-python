price = float(input())
kg = float(input())
days = int(input())
bags_count = int(input())

if kg < 10:
    price *= 0.2
elif kg <= 20:
    price *= 0.5

if days > 30:
    price *= 1.1
elif days < 7:
    price *= 1.4
else:
    price *= 1.15

total = bags_count * price

print(f"The total price of bags is: {total:.2f} lv. ")
