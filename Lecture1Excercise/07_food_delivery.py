CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGETARIAN_MENU = 8.15

chicken_menus_number = int(input())
fish_menus_number = int(input())
vegetarian_menus_number = int(input())

price_without_dessert = chicken_menus_number * CHICKEN_MENU \
    + fish_menus_number * FISH_MENU \
    + vegetarian_menus_number * VEGETARIAN_MENU \

dessert_price = price_without_dessert * 0.2

total_bill = price_without_dessert + dessert_price + 2.50

print(f"{total_bill:.2f}")