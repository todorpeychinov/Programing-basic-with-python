trip_price = float(input())
balance = float(input())
days_count = 0
counter = 0

while True:
    user_input = input()
    money = float(input())
    days_count += 1
    if user_input == "spend":
        if balance < money:
            balance = 0
        else:
            balance -= money
        counter += 1
        if counter == 5:
            print("You can't save the money.")
            print(days_count)
            break
        continue
    if user_input == "save":
        balance += money
        counter = 0
        if balance >= trip_price:
            print(f"You saved the money for {days_count} days.")
            break

