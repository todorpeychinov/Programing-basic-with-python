voucher = int(input())
tickets = 0
others = 0

while True:
    user_input = input()

    if user_input == "End":
        break

    if len(user_input) > 8:
        price = ord(user_input[0]) + ord(user_input[1])
        if price > voucher:
            break
        tickets += 1
    else:
        price = ord(user_input[0])
        if price > voucher:
            break
        others += 1

    voucher -= price

print(tickets)
print(others)

