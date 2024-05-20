people = int(input())
season = input()
bill = 0

if people <= 5:
    if season == "spring":
        bill = people * 50
    elif season == "summer":
        bill = people * 48.5
    elif season == "autumn":
        bill = people * 60
    elif season == "winter":
        bill = people * 86

else:
    if season == "spring":
        bill = people * 48
    elif season == "summer":
        bill = people * 45
    elif season == "autumn":
        bill = people * 49.5
    elif season == "winter":
        bill = people * 85

if season == "summer":
    bill *= 0.85
elif season == "winter":
    bill *= 1.08

print(f"{bill:.2f} leva.")
