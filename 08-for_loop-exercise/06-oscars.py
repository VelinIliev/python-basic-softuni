name_of_actor = input()
points_from_accademy = float(input())
num_of_jury = int(input())

jury_points = points_from_accademy

for x in range(num_of_jury):
    name_of_jury = input()
    point_from_jury = float(input())
    points = (len(name_of_jury) * point_from_jury) / 2
    jury_points += points
    if jury_points >= 1250.5:
        print(f'Congratulations, {name_of_actor} got a nominee for leading role with {jury_points:.1f}!')
        break

if jury_points < 1250.5:
    points_needed = 1250.5 - jury_points
    print(f'Sorry, {name_of_actor} you need {points_needed:.1f} more!')