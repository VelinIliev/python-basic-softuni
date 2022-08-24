vacation_days = int(input())

minutes_play_per_year = 30000
work_days_play = 63
vacation_days_play = 127

work_days = 365 - vacation_days

total_work_days_play = work_days * work_days_play
total_vacation_days_play = vacation_days * vacation_days_play

total_play = total_work_days_play + total_vacation_days_play

if minutes_play_per_year >= total_play:
    resting_minutes = minutes_play_per_year - total_play
    hours = resting_minutes // 60
    minutes = resting_minutes % 60
    print(f'Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
else:
    more_minutes = total_play - minutes_play_per_year
    hours = more_minutes // 60
    minutes = more_minutes % 60
    minutes = more_minutes % 60
    print("Tom will run away")
    print(f'{hours} hours and {minutes} minutes more for play')
