NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
THINNER_PRICE = 5.00

nylon = int(input())
paint_liters = int(input())
thinner_liters = int(input())
painters_working_hours = int(input())

paint_liters += paint_liters * 0.1
nylon += 2

materials_price = nylon * NYLON_PRICE + paint_liters * PAINT_PRICE + thinner_liters * THINNER_PRICE + 0.40
painters_bill = painters_working_hours * materials_price * 0.30

total_sum = materials_price + painters_bill

print(total_sum)