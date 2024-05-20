wins = 0
losts = 0
drawn = 0

for i in range(3):
    user_input = input()
    home_result = int(user_input[0])
    guests_result = int(user_input[2])
    if home_result > guests_result:
        wins += 1
    elif guests_result > home_result:
        losts += 1
    else:
        drawn += 1


print(f"Team won {wins} games.")
print(f"Team lost {losts} games.")
print(f"Drawn games: {drawn}")
