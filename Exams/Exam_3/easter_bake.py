from math import ceil

easter_breads = int(input())
sugar = 0
floor = 0
max_sugar = 0
max_flour = 0

for i in range(easter_breads):
    current_sugar = int(input())
    current_flour = int(input())
    sugar += current_sugar
    floor += current_flour
    if current_flour > max_flour:
        max_flour = current_flour
    if current_sugar > max_sugar:
        max_sugar = current_sugar

floor_packs = ceil(floor / 750)
sugar_packs = ceil(sugar / 950)

print(f"Sugar: {sugar_packs}")
print(f"Flour: {floor_packs}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")