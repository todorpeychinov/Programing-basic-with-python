bill = 0

fruit = input()
size = input()
count = int(input())

if size == "small":
    if fruit == "Watermelon":
        bill = 2 * 56 * count
    elif fruit == "Mango":
        bill = 2 * 36.66 * count
    elif fruit == "Pineapple":
        bill = 2 * 42.1 * count
    elif fruit == "Raspberry":
        bill = 2 * 20 * count

elif size == "big":
    if fruit == "Watermelon":
        bill = 5 * 28.7 * count
    elif fruit == "Mango":
        bill = 5 * 19.6 * count
    elif fruit == "Pineapple":
        bill = 5 * 24.8 * count
    elif fruit == "Raspberry":
        bill = 5 * 15.2 * count

if 400 <= bill <= 1000:
    bill *= 0.85
elif bill > 1000:
    bill *= 0.5

print(f"{bill:.2f} lv.")
