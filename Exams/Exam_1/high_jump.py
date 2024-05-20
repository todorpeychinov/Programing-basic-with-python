goal = int(input())
current_goal = goal - 30
counter = 0
unsuccessful = 0
total_count = 0

while True:
    if unsuccessful == 3:
        print(f"Tihomir failed at {current_goal}cm after {counter} jumps.")
        break
    if current_goal == goal + 5:
        print(f"Tihomir succeeded, he jumped over {goal}cm after {counter} jumps.")
        break
    counter += 1
    jump = int(input())

    if jump > current_goal:
        current_goal += 5
        unsuccessful = 0

    else:
        unsuccessful += 1






