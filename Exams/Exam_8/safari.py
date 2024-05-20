budget = float(input())
nights = int(input())
price_per_night = float(input())
extra_tax_percent = int(input()) / 100

if nights > 7:
    price_per_night *= 0.95

total = nights * price_per_night + budget * extra_tax_percent

if total > budget:
    print(f"{total - budget:.2f} leva needed.")
else:
    print(f"Ivanovi will be left with {budget - total:.2f} leva after vacation.")