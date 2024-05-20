total_matches = 0
wins = 0
looses = 0

while True:
    name_of_tournament = input()
    if name_of_tournament == "End of tournaments":
        break

    matches_num = int(input())
    total_matches += matches_num

    for i in range(1, matches_num + 1):
        team_1_points = int(input())
        team_2_points = int(input())
        if team_1_points > team_2_points:
            print(f"Game {i} of tournament {name_of_tournament}: win with {team_1_points - team_2_points} points.")
            wins += 1
        else:
            print(f"Game {i} of tournament {name_of_tournament}: lost with {team_2_points - team_1_points} points.")
            looses += 1


print(f"{wins / total_matches * 100:.2f}% matches win")
print(f"{looses / total_matches * 100:.2f}% matches lost")



