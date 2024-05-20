painted_eggs = int(input())
max_color = None
max_count = 0
orange = 0
red = 0
blue = 0
green = 0

for i in range(painted_eggs):
    color = input()

    if color == "red":
        red += 1
        if red > max_count:
            max_color = "red"
            max_count = red
    elif color == "green":
        green += 1
        if green > max_count:
            max_color = "green"
            max_count = green
    elif color == "blue":
        blue += 1
        if blue > max_count:
            max_color = "blue"
            max_count = blue
    elif color == "orange":
        orange += 1
        if orange > max_count:
            max_color = "orange"
            max_count = orange

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_count} -> {max_color}")
