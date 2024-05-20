day_of_week = input()

price = 12

if day_of_week == "Wednesday" or day_of_week == "Thursday":
    price = 14
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    price = 16

print(price)

