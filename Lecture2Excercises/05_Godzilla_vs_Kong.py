movie_budget = float(input())
extras_number = int(input())
clothes_price = float(input())

decor_price = movie_budget * 0.1

if extras_number > 150:
    clothes_price = clothes_price - clothes_price * 0.1

total_sum = extras_number * clothes_price + decor_price

if total_sum > movie_budget:
    money_needed = total_sum - movie_budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")

else:
    money_left = movie_budget - total_sum
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")