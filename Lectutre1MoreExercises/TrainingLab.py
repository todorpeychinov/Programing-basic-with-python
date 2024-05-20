w = float(input())
h = float(input())
w = w * 100
h = h * 100
working_places_for_row = ((h-100) // 70)
rows = (w // 120)
places_number = (working_places_for_row * rows) - 3
print(int(places_number))
