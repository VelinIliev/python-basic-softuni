trunk_capacity = float(input())

number_of_suitcases = 0
loaded_volume = 0

while True:
    command = input()
    if command == "End":
        print(f'Congratulations! All suitcases are loaded!')
        break
    else:
        suitcase_volume = float(command)
        number_of_suitcases += 1

    if number_of_suitcases % 3 == 0:
        suitcase_volume *= 1.1

    if loaded_volume + suitcase_volume > trunk_capacity:
        print(f'No more space!')
        number_of_suitcases -= 1
        break
    else:
        loaded_volume += suitcase_volume


print(f'Statistic: {number_of_suitcases} suitcases loaded.')


