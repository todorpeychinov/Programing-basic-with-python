mackerel_price = float(input())
sprat_price = float(input())
bonito_kg = float(input())
safrid_kg = float(input())
mussels_kg = int(input())
bonito_price = mackerel_price + mackerel_price * 0.6
safrid_price = sprat_price + sprat_price * 0.8
total_bill = bonito_kg * bonito_price + safrid_kg * safrid_price + mussels_kg * 7.5
print(f'{total_bill:.2f}')
