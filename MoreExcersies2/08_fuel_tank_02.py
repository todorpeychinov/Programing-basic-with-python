gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

fuel_type = input()
fuel_liters = float(input())
club_card = input()

if club_card == 'Yes':
    gasoline_price -= 0.18
    diesel_price -= 0.12
    gas_price -= 0.08

    if fuel_type == 'Gasoline':
        total_price = gasoline_price * fuel_liters

        if 20 <= fuel_liters <= 25:
            total_price = total_price - total_price * 0.08

        elif fuel_liters > 25:
            total_price = total_price - total_price * 0.1

    if fuel_type == 'Diesel':
        total_price = diesel_price * fuel_liters

        if 20 <= fuel_liters <= 25:
            total_price = total_price - total_price * 0.08

        elif fuel_liters > 25:
            total_price = total_price - total_price * 0.1

    if fuel_type == 'Gas':
        total_price = gas_price * fuel_liters

        if 20 <= fuel_liters <= 25:
            total_price = total_price - total_price * 0.08

        elif fuel_liters > 25:
            total_price = total_price - total_price * 0.1

else:

    if fuel_type == 'Gasoline':
        total_price = gasoline_price * fuel_liters

        if 20 <= fuel_liters <= 25:
            total_price = total_price - total_price * 0.08

        elif fuel_liters > 25:
            total_price = total_price - total_price * 0.1

    if fuel_type == 'Diesel':
        total_price = diesel_price * fuel_liters

        if 20 <= fuel_liters <= 25:
            total_price = total_price - total_price * 0.08

        elif fuel_liters > 25:
            total_price = total_price - total_price * 0.1

    if fuel_type == 'Gas':
        total_price = gas_price * fuel_liters

        if 20 <= fuel_liters <= 25:
            total_price = total_price - total_price * 0.08

        elif fuel_liters > 25:
            total_price = total_price - total_price * 0.1


print(f"{total_price:.2f} lv.")

