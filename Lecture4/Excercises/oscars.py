actor = input()
points_from_academy = float(input())

n = int(input())

for i in range(n):
    name = input()
    points = float(input())
    points_from_academy += (len(name) * points / 2)
    if points_from_academy > 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {points_from_academy:.1f}!")
        break

if(points_from_academy <= 1250.5):
    print(f"Sorry, {actor} you need {1250.5 - points_from_academy:.1f} more!")