weight = int(input())
length = int(input())
height = int(input())

space = weight * length * height
volume = 0

while True:
    user_input = input()
    if user_input == "Done":
        print(f"{space - volume} Cubic meters left.")
        break
    user_input = int(user_input)
    volume += user_input
    if volume > space:
        print(f"No more free space! You need {volume - space} Cubic meters more.")
        break

