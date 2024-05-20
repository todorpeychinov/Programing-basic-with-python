guests = int(input())
price_per_person = float(input())
budget = float(input())

cake_price = budget * 0.1

guests_price = price_per_person * guests

if 10 <= guests <= 15:
    guests_price *= 0.85
elif 15 < guests <= 20:
    guests_price *= 0.8
elif guests > 20:
    guests_price *= 0.75

total = guests_price + cake_price

if total <= budget:
    print(f"It is party time! {budget - total:.2f} leva left.")
else:
    print(f"No party! {total - budget:.2f} leva needed.")