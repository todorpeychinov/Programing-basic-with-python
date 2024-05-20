budget = int(input())
season = input()
fishers_count = int(input())

price = 0

if season == "Spring":
    price = 3000

elif season == "Winter":
    price = 2600

else:
    price = 4200


if fishers_count <= 6:
    price *= 0.90

elif fishers_count <= 11:
    price *= 0.85

elif fishers_count >= 12:
    price *= 0.75


if fishers_count % 2 == 0 and season != "Autumn":
    price *= 0.95

if budget >= price:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")