year_fee = int(input())

basketball_shoes = year_fee - year_fee * 0.4
basketball_clothes = basketball_shoes - basketball_shoes * 0.2
basketball_ball = basketball_clothes / 4
basketball_accessories = basketball_ball / 5

total_sum = year_fee + basketball_shoes + basketball_clothes + basketball_ball + basketball_accessories

print(total_sum)