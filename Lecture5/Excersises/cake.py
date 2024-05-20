length = int(input())
weight = int(input())

cake = length * weight


while True:
    user_input = input()
    if user_input == "STOP":
        print(f"{cake} pieces are left.")
        break
    user_input = int(user_input)
    cake -= user_input
    if cake < 0:
        print(f"No more cake left! You need {abs(cake)} pieces more.")
        break
