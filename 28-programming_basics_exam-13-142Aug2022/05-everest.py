everest_high = 8848
starting_point = 5364
meters_to_climb = everest_high - starting_point
days = 1

continue_climbing = True

while continue_climbing:
    base_camp = input()
    if base_camp == "END":
        continue_climbing = False
        break
    elif base_camp == "Yes":
        days += 1

    meters_climbed = int(input())
    meters_to_climb -= meters_climbed

    if meters_to_climb <= 0:
        continue_climbing = False
        break
    if days == 5:
        continue_climbing = False
        break

if days <= 5 and meters_to_climb <= 0:
    print(f'Goal reached for {days} days!')
else:
    print(f'Failed!')
    reached_high = everest_high - meters_to_climb
    print(f'{reached_high}')