number_of_men = int(input())
number_of_women = int(input())
number_of_tables = int(input())
count_tables = 0

for men in range(1, number_of_men + 1):
    if count_tables == number_of_tables:
        break
    for women in range(1, number_of_women + 1):
        count_tables += 1
        print(f'({men} <-> {women})', end = " ")
        if count_tables == number_of_tables:
            break
