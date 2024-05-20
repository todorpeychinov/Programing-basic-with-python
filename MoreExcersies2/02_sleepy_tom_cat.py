days_off = int(input())
one_year_days = 365
minutes_for_play_norm = 30000

minutes_for_play = (one_year_days - days_off) * 63 + days_off * 127

if minutes_for_play > minutes_for_play_norm:
    overtime_minutes = (minutes_for_play - minutes_for_play_norm)
    hours = overtime_minutes // 60
    minutes = overtime_minutes - hours * 60
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")

else:
    under_time_minutes = (minutes_for_play_norm - minutes_for_play)
    hours = under_time_minutes // 60
    minutes = under_time_minutes - hours * 60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
