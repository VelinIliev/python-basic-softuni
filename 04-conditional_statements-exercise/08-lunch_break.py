from math import ceil, floor

name_of_series = input()
series_duration = int(input())
break_duration = int(input())

time_for_lunch = break_duration / 8
time_for_rest = break_duration / 4

if break_duration >= series_duration + time_for_lunch + time_for_rest:
    time_left = ceil(break_duration - (series_duration + time_for_lunch + time_for_rest))
    print(f'You have enough time to watch {name_of_series} and left with {time_left} minutes free time.')
else:
    time_needed = ceil((series_duration + time_for_lunch + time_for_rest) - break_duration)
    print(f"You don't have enough time to watch {name_of_series}, you need {time_needed} more minutes.")