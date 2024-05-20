money_expected = int(input())
counter = 0
collected_money = 0
sold_cash = 0
sold_card = 0
money_cash = 0
money_card = 0

while True:
    user_input = input()
    counter += 1
    if user_input == "End":
        print("Failed to collect required money for charity.")
        break
    user_input = int(user_input)
    if counter == 1:
        if user_input > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            money_cash += user_input
            sold_cash += 1
            collected_money += user_input
    else:
        counter = 0
        if user_input < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            money_card += user_input
            sold_card += 1
            collected_money += user_input

    if collected_money >= money_expected:
        print(f"Average CS: {money_cash / sold_cash:.2f}")
        print(f"Average CC: {money_card / sold_card:.2f}")
        break






