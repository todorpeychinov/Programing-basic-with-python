price_for_vegetables = float(input())
price_for_fruits = float(input())
vegetables_kg = int(input())
fruits_kg = int(input())
total_price_for_vegetables = price_for_vegetables * vegetables_kg
total_price_for_fruits = price_for_fruits * fruits_kg
total_for_all = total_price_for_fruits + total_price_for_vegetables
total_euro = total_for_all / 1.94
print(f'{total_euro:.2f}')
