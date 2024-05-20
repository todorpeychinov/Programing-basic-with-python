clients = int(input())
total_paid = 0

for i in range(clients):
    items = 0
    total = 0
    while True:
        user_input = input()

        if user_input == "Finish":
            if items % 2 == 0:
                total *= 0.8
            print(f"You purchased {items} items for {total:.2f} leva.")
            total_paid += total
            break
        elif user_input == "basket":
            total += 1.5
        elif user_input == "wreath":
            total += 3.8
        elif user_input == "chocolate bunny":
            total += 7
        items += 1

print(f"Average bill per client is: {total_paid / clients:.2f} leva.")