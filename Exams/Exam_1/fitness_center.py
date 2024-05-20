number_of_people = int(input())

back = 0
chest = 0
abs = 0
legs = 0
protein_shake = 0
protein_bar = 0

for i in range(number_of_people):
    user_input = input()

    if user_input == "Back":
        back += 1
    elif user_input == "Chest":
        chest += 1
    elif user_input == "Abs":
        abs += 1
    elif user_input == "Legs":
        legs += 1
    elif user_input == "Protein shake":
        protein_shake += 1
    elif user_input == "Protein bar":
        protein_bar += 1

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{(back + abs + chest + legs) / number_of_people * 100:.2f}% - work out")
print(f"{(protein_bar + protein_shake) / number_of_people * 100:.2f}% - protein")