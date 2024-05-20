total_walk = 0

while True:
    user_input = input()
    if user_input == "Going home":
        user_input = int(input())
        total_walk += user_input
        break
    else:
        user_input = int(user_input)
        total_walk += user_input
        if total_walk >= 10000:
            break


if total_walk >= 10000:
    print("Goal reached! Good job!")
    print(f"{total_walk - 10000} steps over the goal!")
else:
    print(f"{10000 - total_walk} more steps to reach goal.")