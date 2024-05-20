from math import floor

tournaments_count = int(input())
total_points = int(input())
points = 0
wins = 0

for i in range(tournaments_count):
    user_input = input()

    if user_input == "W":
        points += 2000
        wins += 1
    elif user_input == "F":
        points += 1200
    else:
        points += 720

total_points += points

print(f"Final points: {total_points}")
print(f"Average points: {floor(points / tournaments_count)}")
print(f"{wins / tournaments_count * 100:.2f}%")