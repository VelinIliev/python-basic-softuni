targer_steps = 10000
reached_steps = 0

going_home = False

while reached_steps < 10000:
    steps = input()

    if steps != "Going home":
        steps = int(steps)
        reached_steps += steps

    if going_home == True and reached_steps < 10000:
        print(f'{targer_steps - reached_steps} more steps to reach goal.')
        break
    elif reached_steps >= 10000 or going_home == True:
        print("Goal reached! Good job!")
        print(f'{reached_steps - targer_steps} steps over the goal!')

    if steps == "Going home":
        going_home = True