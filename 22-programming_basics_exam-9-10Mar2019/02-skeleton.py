pass_check_minutes = int(input())
pass_check_seconds = int(input())
chute_length = float(input())
seconds_per_100m = int(input())

pass_check_in_seconds = pass_check_minutes * 60 + pass_check_seconds

delay_times = chute_length / 120

delay_time = delay_times * 2.5

marin_time = (chute_length / 100) * seconds_per_100m - delay_time


if marin_time <= pass_check_in_seconds:
    print(f'Marin Bangiev won an Olympic quota!')
    print(f'His time is {marin_time:.3f}.')
else:
    print(f'No, Marin failed! He was {marin_time - pass_check_in_seconds:.3f} second slower.')