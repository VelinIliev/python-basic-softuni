starting_base_camp = 5364
everest_high = 8848

days = 1
goal_reached = False

while True:
    base_camp = input()
    if base_camp == "END":
        break
    elif base_camp == "Yes":
        days += 1

    if days > 5:
        break

    meters_climbed = int(input())
    starting_base_camp += meters_climbed

    if starting_base_camp >= everest_high:
        goal_reached = True
        print(f'Goal reached for {days} days!')
        break

if not goal_reached:
    print("Failed!")
    print(f"{starting_base_camp}")