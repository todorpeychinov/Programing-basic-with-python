from math import floor, ceil

tennis_rocket_price = float(input())
tennis_rocket_count = int(input())
trainers_count = int(input())

trainers_price = 1/6 * tennis_rocket_price

trainers_and_rocket_price = tennis_rocket_price * tennis_rocket_count + trainers_price * trainers_count
other_equipment_price = trainers_and_rocket_price * 0.2
total_price = trainers_and_rocket_price + other_equipment_price

print(f"Price to be paid by Djokovic {floor(1/8 * total_price)}")
print(f"Price to be paid by sponsors {ceil(7/8 * total_price)}")