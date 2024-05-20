eggs = int(input())
sold_eggs = 0

while True:
    user_input = input()
    if user_input == "Close":
        print("Store is closed!")
        print(f"{sold_eggs} eggs sold.")
        break
    egg = int(input())

    if user_input == "Buy":
        if eggs >= egg:
            eggs -= egg
            sold_eggs += egg
        else:
            print("Not enough eggs in store!")
            print(f"You can buy only {eggs}.")
            break
    elif user_input == "Fill":
        eggs += egg

