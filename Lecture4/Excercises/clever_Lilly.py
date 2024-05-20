age = int(input())
washing_machine_price = float(input())
toys_price = int(input())
toys_count = 0
money = 10

savings = 0

for i in range(1, age + 1):
    if i % 2 != 0:
        toys_count += 1
    else:
        savings += money
        money += 10
        savings -= 1

savings += toys_count * toys_price

if savings >= washing_machine_price:
    print(f"Yes! {savings - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - savings:.2f}")

