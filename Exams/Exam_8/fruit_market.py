strawberries_price = float(input())
bananas = float(input())
oranges = float(input())
raspberries = float(input())
strawberries = float(input())

raspberries_price = strawberries_price / 2
oranges_price = 0.6 * raspberries_price
bananas_price = 0.2 * raspberries_price

total = strawberries_price * strawberries + bananas_price * bananas + \
        oranges_price * oranges + raspberries_price * raspberries

print(f"{total:.2f}")