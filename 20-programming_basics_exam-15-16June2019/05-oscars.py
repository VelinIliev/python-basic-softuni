
name_of_actor = input()
academy_points = float(input())
jury_members = int(input())

points_collected = academy_points

for member in range(jury_members):
    name_of_member = input()
    points = float(input())
    member_points = len(name_of_member) * points / 2
    points_collected += member_points
    if points_collected > 1250.5:
        print(f'Congratulations, {name_of_actor} got a nominee for leading role with {points_collected:.1f}!')
        break

if points_collected <= 1250.5:
    print(f'Sorry, {name_of_actor} you need {1250.5 - points_collected:.1f} more!')
