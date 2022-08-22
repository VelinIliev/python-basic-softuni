while True:
    destination = input()
    if destination == "End":
        break
    min_budget = float(input())
    savings = 0

    while savings < min_budget:
        income = float(input())
        savings += income

        if savings >= min_budget:
            print(f'Going to {destination}!')
            break