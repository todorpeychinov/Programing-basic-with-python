sea_excursion_count = int(input())
mountain_excursion_count = int(input())
profit = 0

while True:
    packet = input()

    if packet == "Stop":
        break
    elif packet == "sea":
        if sea_excursion_count > 0:
            sea_excursion_count -= 1
            profit += 680
    elif packet == "mountain":
        if mountain_excursion_count > 0:
            mountain_excursion_count -= 1
            profit += 499

    if mountain_excursion_count == 0 and sea_excursion_count == 0:
        print("Good job! Everything is sold.")
        break

print(f"Profit: {profit} leva.")
