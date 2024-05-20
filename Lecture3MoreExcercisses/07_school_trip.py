season = input()
group_type = input()
students = int(input())
nights = int(input())
sport = ""


if group_type == "boys" or group_type == "girls":
    if season == "Winter":
        price = 9.6
    elif season == "Spring":
        price = 7.2
    elif season == "Summer":
        price = 15
else:
    if season == "Winter":
        price = 10
    elif season == "Spring":
        price = 9.5
    elif season == "Summer":
        price = 20

if group_type == "girls":
    if season == "Winter":
        sport = "Gymnastics"
    elif season == "Spring":
        sport = "Athletics"
    elif season == "Summer":
        sport = "Volleyball"
elif group_type == "boys":
    if season == "Winter":
        sport = "Judo"
    elif season == "Spring":
        sport = "Tennis"
    elif season == "Summer":
        sport = "Football"
else:
    if season == "Winter":
        sport = "Ski"
    elif season == "Spring":
        sport = "Cycling"
    elif season == "Summer":
        sport = "Swimming"

total_price = students * price * nights

if 10 <= students < 20:
    total_price -= total_price * 0.05
elif 20 <= students < 50:
    total_price -= total_price * 0.15
elif 50 <= students:
    total_price -= total_price * 0.5

print(f"{sport} {total_price:.2f} lv.")