video_card_price = 250

budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memmory = int(input())

total_video_cards_price = video_cards * video_card_price
processors_price = total_video_cards_price * 0.35
ram_memmory_price = total_video_cards_price * 0.1

total_bill = video_cards * video_card_price + processors * processors_price + ram_memmory * ram_memmory_price

if video_cards > processors:
    total_bill = total_bill - total_bill * 0.15

if budget >= total_bill:
    money_left = budget - total_bill
    print(f"You have {money_left:.2f} leva left!")

else:
    money_needed = total_bill - budget
    print(f"Not enough money! You need {money_needed:.2f} leva more!")