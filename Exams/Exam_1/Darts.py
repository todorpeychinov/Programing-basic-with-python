name = input()
total_points = 301
successful = 0
unsuccessful = 0

while True:
    type = input()

    if type == "Retire":
        print(f"{name} retired after {unsuccessful} unsuccessful shots.")
        break

    points = int(input())

    if type == "Single":

        if points > total_points:
            unsuccessful += 1
            continue
        else:
            total_points -= points
            successful += 1

    elif type == "Double":
        if points * 2 > total_points:
            unsuccessful += 1
            continue
        else:
            total_points -= points * 2
            successful += 1

    else:
        if points * 3 > total_points:
            unsuccessful += 1
            continue
        else:
            total_points -= points * 3
            successful += 1

    if total_points == 0:
        print(f"{name} won the leg with {successful} shots.")
        break