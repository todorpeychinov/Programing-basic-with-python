eggs_player_1 = int(input())
eggs_player_2 = int(input())

while True:
    user_input = input()
    if user_input == "End":
        print(f"Player one has {eggs_player_1} eggs left.")
        print(f"Player two has {eggs_player_2} eggs left.")
        break

    elif user_input == "one":
        eggs_player_2 -= 1

    else:
        eggs_player_1 -= 1

    if eggs_player_1 == 0:
        print(f"Player one is out of eggs. Player two has {eggs_player_2} eggs left.")
        break
    elif eggs_player_2 == 0:
        print(f"Player two is out of eggs. Player one has {eggs_player_1} eggs left.")
        break
