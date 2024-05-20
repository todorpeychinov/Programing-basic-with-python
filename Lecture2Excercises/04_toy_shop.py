puzzle_price = 2.60
doll_price = 3.00
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2.00

travel_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

total_price = puzzles_count * puzzle_price + dolls_count * doll_price + teddy_bears_count * teddy_bear_price \
              + minions_count * minion_price + trucks_count * truck_price \

number_of_toys = puzzles_count + dolls_count + teddy_bears_count + minions_count + trucks_count

if number_of_toys >= 50:
    total_price = total_price - total_price * 0.25

total_profit = total_price - total_price * 0.1

if total_profit >= travel_price:
    money_left = total_profit - travel_price
    print(f"Yes! {money_left:.2f} lv left.")

else:
    needed_money = travel_price - total_profit
    print(f"Not enough money! {needed_money:.2f} lv needed.")
