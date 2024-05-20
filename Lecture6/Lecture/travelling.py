money = 0

while True:
    destination = input()
    if destination == "End":
        break
    price = float(input())
    while money < price:
        money += float(input())
        if money >= price:
            print(f"Going to {destination}!")
            money = 0
            break


