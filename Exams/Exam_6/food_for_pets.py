biscuits_eaten = 0
dog_food = 0
cat_food = 0

days = int(input())
total_food = float(input())

for i in range(1, days + 1):
    dog = int(input())
    cat = int(input())

    if i % 3 == 0:
        biscuits_eaten += (dog + cat) * 0.1

    dog_food += dog
    cat_food += cat

cat_and_dog = dog_food + cat_food

print(f"Total eaten biscuits: {round(biscuits_eaten)}gr.")
print(f"{(cat_and_dog / total_food) * 100:.2f}% of the food has been eaten.")
print(f"{(dog_food  / cat_and_dog) * 100:.2f}% eaten from the dog.")
print(f"{(cat_food  / cat_and_dog) * 100:.2f}% eaten from the cat.")

