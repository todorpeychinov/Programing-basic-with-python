balance = 0

while True:
    user_input = input()
    if user_input == "NoMoreMoney":
        break
    user_input = float(user_input)
    if user_input < 0:
        print("Invalid operation!")
        break
    balance += user_input
    print(f"Increase: {user_input:.2f}")

print(f"Total: {balance:.2f}")

