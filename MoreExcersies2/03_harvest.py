from math import floor, ceil

square_meters = int(input())
grape_for_square_meter = float(input())
wine_liters_needed = int(input())
workers_number = int(input())

grape_produced = square_meters * grape_for_square_meter
grape_for_wine = grape_produced * 0.4
liters_wine = grape_for_wine / 2.5

if liters_wine < wine_liters_needed:
    lacking_wine = wine_liters_needed - liters_wine
    print(f"It will be a tough winter! More {floor(lacking_wine)} liters wine needed.")
else:
    wine_left = liters_wine - wine_liters_needed
    wine_for_one_worker = wine_left / workers_number
    print(f"Good harvest this year! Total wine: {floor(liters_wine)} liters.")
    print(f"{ceil(wine_left)} liters left -> {ceil(wine_for_one_worker)} liters per person.")

