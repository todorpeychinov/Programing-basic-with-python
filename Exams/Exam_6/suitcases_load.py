capacity = float(input())
filled_capacity = 0
counter = 0
bags = 0

while True:
    user_input = input()
    counter += 1

    if user_input == "End":
        print("Congratulations! All suitcases are loaded!")
        break

    user_input = float(user_input)

    if counter % 3 == 0:
        user_input += user_input * 0.1

    if user_input > capacity:
        print("No more space!")
        break
    capacity -= user_input
    bags += 1

print(f"Statistic: {bags} suitcases loaded.")