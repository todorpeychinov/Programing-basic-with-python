flowers_type1 = int(input())
flowers_type2 = int(input())
flowers_type3 = int(input())
season = input()
holiday = input()

flowers_type1_price = 0
flowers_type2_price = 0
flowers_type3_price = 0
total_sum = 0

if season == "Spring" or season == "Summer":
    flowers_type1_price = 2
    flowers_type2_price = 4.1
    flowers_type3_price = 2.5
    total_sum = flowers_type1 * flowers_type1_price + flowers_type2 * flowers_type2_price + \
                flowers_type3 * flowers_type3_price
    if holiday == "Y":
        total_sum += total_sum * 0.15
    if flowers_type3 > 7 and season == "Spring":
        total_sum -= total_sum * 0.05
    if flowers_type1 + flowers_type2 + flowers_type3 > 20:
        total_sum -= total_sum * 0.2

elif season == "Autumn" or season == "Winter":
    flowers_type1_price = 3.75
    flowers_type2_price = 4.5
    flowers_type3_price = 4.15
    total_sum = flowers_type1 * flowers_type1_price + flowers_type2 * flowers_type2_price + \
                flowers_type3 * flowers_type3_price
    if holiday == "Y":
        total_sum += total_sum * 0.15
    if flowers_type2 >= 10 and season == "Winter":
        total_sum -= total_sum * 0.1
    if flowers_type1 + flowers_type2 + flowers_type3 > 20:
        total_sum -= total_sum * 0.2

print(f"{total_sum + 2:.2f}")