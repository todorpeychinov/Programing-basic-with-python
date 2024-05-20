from math import floor

n = int(input())
points = 0
red = 0
orange = 0
yellow = 0
white = 0
black = 0
other = 0


for i in range(n):
    ball = input()
    if ball == "red":
        points += 5
        red += 1
    elif ball == "orange":
        points += 10
        orange += 1
    elif ball == "yellow":
        points += 15
        yellow += 1
    elif ball == "white":
        points += 20
        white += 1
    elif ball == "black":
        points = floor(points / 2)
        black += 1
    else:
        other += 1


print(f"Total points: {points}")
print(f"Red balls: {red}")
print(f"Orange balls: {orange}")
print(f"Yellow balls: {yellow}")
print(f"White balls: {white}")
print(f"Other colors picked: {other}")
print(f"Divides from black balls: {black}")

