season = input()
kilometers = float(input())
price = 0

if season == "Summer":
    if kilometers <= 5000:
        price = 0.9
    elif 5000 < kilometers <= 10000:
        price = 1.1
    else:
        price = 1.45
elif season == "Winter":
    if kilometers <= 5000:
        price = 1.05
    elif 5000 < kilometers <= 10000:
        price = 1.25
    else:
        price = 1.45
else:
    if kilometers <= 5000:
        price = 0.75
    elif 5000 < kilometers <= 10000:
        price = 0.95
    else:
        price = 1.45



total_price = 4 *price * kilometers
total_price -= total_price * 0.1

print(f"{total_price:.2f}")