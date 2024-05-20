rent = int(input())
oscars_price = 0.7  * rent
catering = 0.85 * oscars_price
sound = 0.5 * catering

total = rent + oscars_price + catering + sound
print(f"{total:.2f}")