turns = int(input())
points = 0
invalid = 0;
forty_to_fifty = 0
thirty_to_thirty_nine = 0
twenty_to_twenty_nine = 0
ten_to_nineteen = 0
zero_to_nine = 0



for i in range(turns):
    number = int(input())

    if number < 0 or number > 50:
        points = points / 2
        invalid += 1

    elif 40 <= number <= 50:
        points += 100
        forty_to_fifty += 1

    elif 30 <= number <= 39:
        points += 50
        thirty_to_thirty_nine += 1

    elif 20 <= number <= 29:
        points += 0.4 * number
        twenty_to_twenty_nine += 1

    elif 10 <= number <= 19:
        points += 0.3 * number
        ten_to_nineteen += 1

    elif 0 <= number <= 9:
        points += 0.2 * number
        zero_to_nine += 1


percent1 = zero_to_nine / turns * 100
percent2 = ten_to_nineteen / turns * 100
percent3 = twenty_to_twenty_nine / turns * 100
percent4 = thirty_to_thirty_nine / turns * 100
percent5 = forty_to_fifty / turns * 100
percent6 = invalid / turns * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {percent1:.2f}%")
print(f"From 10 to 19: {percent2:.2f}%")
print(f"From 20 to 29: {percent3:.2f}%")
print(f"From 30 to 39: {percent4:.2f}%")
print(f"From 40 to 50: {percent5:.2f}%")
print(f"Invalid numbers: {percent6:.2f}%")





