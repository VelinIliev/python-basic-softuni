wall_height = int(input())
wall_width = int(input())
percent_for_no_paint = int(input())

wall_area = wall_width * wall_height
total_walls = wall_area * 4
total_walls_to_paint = total_walls - total_walls * percent_for_no_paint / 100

while total_walls_to_paint >= 0 :
    paint_litters = input()
    if paint_litters == "Tired!":
        print(f'{int(total_walls_to_paint)} quadratic m left.')
        break
    else:
        paint_litters = int(paint_litters)

    total_walls_to_paint -= paint_litters

    if total_walls_to_paint <= 0:
        if total_walls_to_paint == 0:
            print("All walls are painted! Great job, Pesho!")
            break
        else:
            print(f'All walls are painted and you have {int(abs(total_walls_to_paint))} l paint left!')
            break
