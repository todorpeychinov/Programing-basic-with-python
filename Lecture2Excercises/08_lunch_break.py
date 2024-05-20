from math import ceil

series = input()
episode_duration = int(input())
break_time = int(input())

time_for_lunch = break_time / 8
time_for_relax = break_time / 4

left_time = break_time - (time_for_lunch  + time_for_relax)

if left_time >= episode_duration:

    free_time = left_time - episode_duration
    print(f"You have enough time to watch {series} and left with {ceil(free_time)} minutes free time.")

else:

    time_needed = episode_duration - left_time
    print(f"You don't have enough time to watch {series}, you need {ceil(time_needed)} more minutes.")

