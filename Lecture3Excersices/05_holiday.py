budget = float(input())
season = input()

sitting_type = None
destination = None

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.3
        sitting_type = "Camp"
    else:
        price = budget * 0.7
        sitting_type = "Hotel"

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.4
        sitting_type = "Camp"
    else:
        price = budget * 0.8
        sitting_type = "Hotel"

else:
    price = budget * 0.9
    destination = "Europe"
    sitting_type = "Hotel"

print(f"Somewhere in {destination}")
print(f"{sitting_type} - {price:.2f}")