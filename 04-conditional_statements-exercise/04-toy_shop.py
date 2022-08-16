puzzle = 2.60
doll = 3.00
teddy_bear = 4.10
minion = 8.20
truck = 2.00

excursion_price = float(input())

no_puzzles = int(input())
no_dolls = int(input())
no_teddy_bears = int(input())
no_minions = int(input())
no_trucks = int(input())

total_toys = no_puzzles + no_dolls + no_teddy_bears + no_minions + no_trucks

total_price = (puzzle * no_puzzles) + (doll * no_dolls) + (teddy_bear * no_teddy_bears) + (minion * no_minions) + (truck * no_trucks)

if total_toys >= 50:
    total_price = total_price * .75

rent = total_price * .1

money_after_rent = total_price - rent

go_to_excursion = money_after_rent - excursion_price

if go_to_excursion >= 0:
    go_to_excursion = round(go_to_excursion,2)
    print(f'Yes! {go_to_excursion:.02f} lv left.')
else:
    go_to_excursion = round(go_to_excursion*-1,2)
    print(f'Not enough money! {go_to_excursion:.02f} lv needed.')