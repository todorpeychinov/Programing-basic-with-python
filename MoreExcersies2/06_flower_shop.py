from math import ceil, floor

magnolias_price = 3.25
hyacinth_price = 4
roses_price = 3.5
cactus_price = 8

number_of_magnolias = int(input())
number_of_hyacinths = int(input())
number_of_roses = int(input())
number_of_cacti = int(input())
present_price = float(input())

total_bill = number_of_magnolias * magnolias_price + \
    number_of_hyacinths * hyacinth_price + \
    number_of_roses * roses_price + \
    number_of_cacti * cactus_price \

total_profit = total_bill - total_bill * 0.05

if total_profit >= present_price:
    money_left = total_profit - present_price
    print(f"She is left with {floor(money_left)} leva.")

else:
    money_needed = present_price - total_profit
    print(f"She will have to borrow {ceil(money_needed)} leva.")

