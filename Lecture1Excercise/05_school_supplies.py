PENS_PRICE = 5.80
MARKERS_PRICE = 7.20
CLEANER_PRICE = 1.20

pens_packs = int(input())
markers_packs = int(input())
cleaner_liters = int(input())
discount_percent = int(input()) / 100

price_without_discount = pens_packs * PENS_PRICE \
    + markers_packs * MARKERS_PRICE \
    + cleaner_liters * CLEANER_PRICE \

price_with_discount = price_without_discount - price_without_discount * discount_percent

print(price_with_discount)