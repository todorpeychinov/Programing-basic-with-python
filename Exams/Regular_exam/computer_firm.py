computers_count = int(input())
total_rating = 0
total_sales = 0

for i in range(computers_count):
    number = int(input())
    rating = number % 10
    sales = number // 10

    if rating == 2:
        sales *= 0
    elif rating == 3:
        sales *= 0.5
    elif rating == 4:
        sales *= 0.7
    elif rating == 5:
        sales *= 0.85

    total_sales += sales
    total_rating += rating

print(f"{total_sales:.2f}")
print(f"{total_rating / computers_count:.2f}")
