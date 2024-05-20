fuel_type = input()
fuel_in_the_tank = float(input())

if fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas":

    if fuel_type == "Diesel":
        fuel_type = "diesel"

        if fuel_in_the_tank >= 25:
            print(f"You have enough {fuel_type}.")
        else:
            print(f"Fill your tank with {fuel_type}!")

    if fuel_type == "Gasoline":
        fuel_type = "gasoline"

        if fuel_in_the_tank >= 25:
            print(f"You have enough {fuel_type}.")
        else:
            print(f"Fill your tank with {fuel_type}!")

    if fuel_type == "Gas":
        fuel_type = "gas"

        if fuel_in_the_tank >= 25:
            print(f"You have enough {fuel_type}.")
        else:
            print(f"Fill your tank with {fuel_type}!")


else:
    print("Invalid fuel!")
