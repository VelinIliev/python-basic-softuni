number_of_1lv = int(input())
number_of_2lv = int(input())
number_of_5lv = int(input())
sum = int(input())

for lv1 in range(number_of_1lv + 1):
    for lv2 in range(number_of_2lv + 1):
        for lv5 in range(number_of_5lv + 1):
            if 1 * lv1 + 2 * lv2 + 5 * lv5 == sum:
                print(f"{lv1} * 1 lv. + {lv2} * 2 lv. + {lv5} * 5 lv. = {sum} lv.")
