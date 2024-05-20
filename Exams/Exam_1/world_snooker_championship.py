stage = input()
ticket_type = input()
ticket_count = int(input())
photo = input()
ticket_price = 0

price = 0

if stage == "Quarter final":

    if ticket_type == "Standard":
        ticket_price = 55.5

    elif ticket_type == "Premium":
        ticket_price = 105.2

    elif ticket_type == "VIP":
        ticket_price = 118.9

elif stage == "Semi final":

    if ticket_type == "Standard":
        ticket_price = 75.88

    elif ticket_type == "Premium":
        ticket_price = 125.22

    elif ticket_type == "VIP":
        ticket_price = 300.4

elif stage == "Final":

    if ticket_type == "Standard":
        ticket_price = 110.1

    elif ticket_type == "Premium":
        ticket_price = 160.66

    elif ticket_type == "VIP":
        ticket_price = 400

total_sum = ticket_price * ticket_count

if total_sum > 4000:
    total_sum -= total_sum * 0.25

else:
    if total_sum > 2500:
        total_sum -= total_sum * 0.1
    if photo == "Y":
        total_sum += ticket_count * 40


print(f'{total_sum:.2f}')
