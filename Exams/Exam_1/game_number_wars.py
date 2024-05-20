player_1 = input()
player_2 = input()
points_player_1 = 0
points_player_2 = 0

while True:
    card_player_1 = input()

    if card_player_1 == "End of game":
        print(f"{player_1} has {points_player_1} points")
        print(f"{player_2} has {points_player_2} points")
        break

    card_player_1 = int(card_player_1)
    card_player_2 = int(input())

    if card_player_1 > card_player_2:
        points_player_1 += card_player_1 - card_player_2

    elif card_player_2 > card_player_1:
        points_player_2 += card_player_2 - card_player_1

    else:
        card_player_1 = int(input())
        card_player_2 = int(input())
        print("Number wars!")

        if card_player_1 > card_player_2:
            print(f"{player_1} is winner with {points_player_1} points")
            break
        else:
            print(f"{player_2} is winner with {points_player_2} points")
            break



