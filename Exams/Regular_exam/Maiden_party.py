maiden_party_price = float(input())
love_letters = int(input())
roses = int(input())
key_holders = int(input())
caricatures = int(input())
gifts = int(input())

total_count = love_letters + roses + key_holders + caricatures + gifts
bill = love_letters * 0.6 + roses * 7.2 + key_holders * 3.6 + caricatures * 18.2 + gifts * 22

if total_count >= 25:
    bill -= bill * 0.35

profit = bill * 0.9

if profit >= maiden_party_price:
    print(f"Yes! {profit - maiden_party_price:.2f} lv left.")
else:
    print(f"Not enough money! {maiden_party_price - profit:.2f} lv needed.")