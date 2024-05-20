budget = float(input())
season = input()

settlement = ""
location = ""
price = 0

if budget <= 1000:
    settlement = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    else:
        location = "Morocco"
        price = budget * 0.45

elif 1000 < budget <= 3000:
    settlement = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.8
    else:
        location = "Morocco"
        price = budget * 0.6
elif 3000 < budget:
    settlement = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.9
    else:
        location = "Morocco"
        price = budget * 0.9

print(f"{location} - {settlement} - {price:.2f}")

