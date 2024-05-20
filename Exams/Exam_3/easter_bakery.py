price_floor = float(input())
kg_floor = float(input())
kg_sugar = float(input())
eggs = int(input())
yeast = int(input())

price_sugar = price_floor * 0.75
price_eggs = price_floor * 1.1
price_yeast = 0.2 * price_sugar

total = price_floor * kg_floor + price_sugar * kg_sugar + price_eggs * eggs\
        + price_yeast * yeast

print(f"{total:.2f}")