from math import floor, ceil

days = int(input())
kg_food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input()) / 1000

needed_food = (dog_food_per_day + cat_food_per_day + turtle_food_per_day) * days

if needed_food <= kg_food:
    food_left = kg_food - needed_food
    print(f"{floor(food_left)} kilos of food left.")

else:
    lack_of_food = needed_food - kg_food
    print(f"{ceil(lack_of_food)} more kilos of food are needed.")

