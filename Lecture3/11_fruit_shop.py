fruit = input()
day_of_week = input()
qty = float(input())

result = "error"

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" \
    or day_of_week == "Thursday" or day_of_week == "Friday":
    if fruit == "banana":
        result = qty * 2.5
    elif fruit == "apple":
        result = qty * 1.2
    elif fruit == "orange":
        result = qty * 0.85
    elif fruit == "grapefruit":
        result = qty * 1.45
    elif fruit == "kiwi":
        result = qty * 2.70
    elif fruit == "pineapple":
        result = qty * 5.5
    elif fruit == "grapes":
        result = qty * 3.85
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        result = qty * 2.7
    elif fruit == "apple":
        result = qty * 1.25
    elif fruit == "orange":
        result = qty * 0.9
    elif fruit == "grapefruit":
        result = qty * 1.6
    elif fruit == "kiwi":
        result = qty * 3
    elif fruit == "pineapple":
        result = qty * 5.6
    elif fruit == "grapes":
        result = qty * 4.2

if result != "error":
    print(f"{result:.2f}")
else:
    print(result)