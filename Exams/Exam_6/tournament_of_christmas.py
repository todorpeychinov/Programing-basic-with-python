days = int(input())
daily_wins = 0
daily_looses = 0
days_win = 0
days_loose = 0
total_money = 0

for i in range(days):
    daily_wins = 0
    daily_looses = 0
    daily_money = 0
    while True:
        user_input = input()
        if user_input == "Finish":
            break
        result = input()

        if result == "win":
            daily_money += 20
            daily_wins += 1
        else:
            daily_looses += 1

    if daily_wins > daily_looses:
        daily_money += daily_money * 0.1
        days_win += 1
    else:
        days_loose += 1

    total_money += daily_money

if days_win > days_loose:
    total_money += total_money * 0.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")