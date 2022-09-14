starting_number_of_eggs = int(input())

available_eggs = starting_number_of_eggs
sold_eggs = 0

while True:
    operation = input()
    if operation == "Close":
        print(f'Store is closed!')
        print(f'{sold_eggs} eggs sold.')
        break
    else:
        number_of_eggs = int(input())

        if operation == "Buy" and available_eggs - number_of_eggs >= 0:
            sold_eggs += number_of_eggs
            available_eggs -= number_of_eggs
        elif operation == "Fill":
            available_eggs += number_of_eggs
        elif operation == "Buy" and available_eggs - number_of_eggs < 0:
            print(f'Not enough eggs in store!')
            print(f'You can buy only {available_eggs}.')
            break

