months_count = int(input())
total_electricity = 0
other = 0

for i in range(months_count):
    electricity_bill = float(input())
    total_electricity += electricity_bill
    other += ((electricity_bill + 20 + 15) * 1.2)

total_water = months_count * 20
total_internet = months_count * 15
average = (total_internet + total_water + total_electricity + other) / months_count

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {average:.2f} lv")


