projection_type = input()
rows = int(input())
columns = int(input())

total_places = rows * columns

if projection_type == "Premiere":
    price = 12

elif projection_type == "Normal":
    price = 7.5

elif projection_type == "Discount":
    price = 5

total_sum = total_places * price

print(f"{total_sum:.2f} leva")