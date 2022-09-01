series_name = input()
seasons = int(input())
episodes = int(input())
duration_without_ads = float(input())

duration_with_ads = duration_without_ads * 1.2

total_time = seasons * episodes * duration_with_ads + seasons * 10

print(f'Total time needed to watch the {series_name} series is {int(total_time)} minutes.')