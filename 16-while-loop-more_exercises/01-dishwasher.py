number_of_bottles = int(input())

bottle = 750
dish = 5
pot = 15
loading = 0

left_over_detergent = number_of_bottles * bottle
dishes_washed = 0
pots_washed = 0


while left_over_detergent >= 0:
    loading += 1
    number_of_dishes = input()
    if number_of_dishes == "End":
        print(f'Detergent was enough!')
        print(f'{dishes_washed} dishes and {pots_washed} pots were washed.')
        print(f'Leftover detergent {left_over_detergent} ml.')
        break
    else:
        number_of_dishes = int(number_of_dishes)

    if loading % 3 == 0:
        detergent_needed = number_of_dishes * pot
        pots_washed += number_of_dishes
        left_over_detergent -= detergent_needed
    else:
        detergent_needed = number_of_dishes * dish
        dishes_washed += number_of_dishes
        left_over_detergent -= detergent_needed

    if left_over_detergent < 0:
        print(f'Not enough detergent, {abs(left_over_detergent)} ml. more necessary!')
        break

