nights = int(input()) - 1
type_of_room = input()
review = input()

if type_of_room == "room for one person":
    price = 18

elif type_of_room == "apartment":
    price = 25
    if nights < 10:
        price *= 0.70
    elif nights <= 15:
        price *= 0.65
    else:
        price *= 0.5

elif type_of_room == "president apartment":
    price = 35
    if nights < 10:
        price *= 0.90
    elif nights <= 15:
        price *= 0.85
    else:
        price *= 0.80

if review == "positive":
    price *= 1.25

else:
    price *= 0.90

print(f'{price * nights:.2f}')