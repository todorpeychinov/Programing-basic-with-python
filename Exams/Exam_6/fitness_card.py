card_price = 0

money = float(input())
gender = input()
age = int(input())
sport = input()

if gender == "m":
    if sport == "Gym":
        card_price = 42
    elif sport == "Boxing":
        card_price = 41
    elif sport == "Yoga":
        card_price = 45
    elif sport == "Zumba":
        card_price = 34
    elif sport == "Dances":
        card_price = 51
    elif sport == "Pilates":
        card_price = 39

elif gender == "f":
    if sport == "Gym":
        card_price = 35
    elif sport == "Boxing":
        card_price = 37
    elif sport == "Yoga":
        card_price = 42
    elif sport == "Zumba":
        card_price = 31
    elif sport == "Dances":
        card_price = 53
    elif sport == "Pilates":
        card_price = 37

if age <= 19:
    card_price -= card_price * 0.2

if money >= card_price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${card_price - money:.2f} more.")

