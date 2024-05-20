food = int(input()) * 1000

while True:
    user_input = input()

    if user_input == "Adopted":
        break

    user_input = int(user_input)
    food -= user_input


if food < 0:
    print(f"Food is not enough. You need {abs(food)} grams more.")
else:
    print(f"Food is enough! Leftovers: {food} grams.")