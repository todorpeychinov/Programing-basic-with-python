year_fee = float(input())
trainers_price = 0.6 * year_fee
basketball_clothes_price = trainers_price * 0.8
basketball_ball_price = 1/4 * basketball_clothes_price
basketball_accessories = 1/5 * basketball_ball_price

total_price = year_fee + trainers_price + basketball_clothes_price + basketball_ball_price + basketball_accessories

print(f"{total_price:.2f}")