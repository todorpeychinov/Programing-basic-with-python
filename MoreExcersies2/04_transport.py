kilometers = int(input())
part_of_the_day = input()

if kilometers < 20:

    if part_of_the_day == 'day':
        price = 0.7 + 0.79 * kilometers
    else:
        price = 0.7 + 0.9 * kilometers

elif kilometers < 100:
    price = kilometers * 0.09

else:
    price = kilometers * 0.06

print(f"{price:.2f}")

