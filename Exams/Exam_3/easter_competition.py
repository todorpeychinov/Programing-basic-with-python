easter_breads = int(input())

points = 0
max_points = 0
max_name = None

for i in range(easter_breads):
    name = input()
    points = 0
    while True:
        user_input = input()
        if user_input == "Stop":
            print(f"{name} has {points} points.")
            if points > max_points:
                print(f"{name} is the new number 1!")
                max_points = points
                max_name = name
            break
        else:
            user_input = int(user_input)
            points += user_input

print(f"{max_name} won competition with {max_points} points!")