budget = float(input())
season = input()
car_class = ""
car_type = ""
price = 0

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        price = budget * 0.35
    else:
        price = budget * 0.65
        car_type = "Jeep"
elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        price = budget * 0.45
        car_type = "Cabrio"
    else:
        price = budget * 0.8
        car_type = "Jeep"
elif budget > 500:
    car_class = "Luxury class"
    car_type = "Jeep"
    price = budget * 0.9

print(car_class)
print(f"{car_type} - {price:.2f}")



