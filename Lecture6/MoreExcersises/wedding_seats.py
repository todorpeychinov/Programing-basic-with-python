sectors = input()
rows = int(input())
places_odd = int(input())
places = 0

for sector in range(ord("A"), ord(sectors) + 1):
    for row in range(1, rows + 1):
        if row % 2 == 0:
            for place_odd in range(ord("a"), (ord("a") + places_odd + 2)):
                print(f"{chr(sector)}{row}{chr(place_odd)}")
                places += 1
        else:
            for place in range(ord("a"), ord("a") + places_odd):
                print(f"{chr(sector)}{row}{chr(place)}")
                places += 1
    rows += 1

print(places)