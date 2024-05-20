from math import floor

turners = int(input())
points = float(input())
win = 0
start_points = points

for i in range(turners):
    finish = input()
    if finish == "W":
        points += 2000
        win += 1
    elif finish == "F":
        points += 1200
    elif finish == "SF":
        points += 720

print(f"Final points: {int(points)}")
print(f"Average points: {floor((points - start_points)/ turners)}")
print(f"{win / turners * 100:.2f}%")

