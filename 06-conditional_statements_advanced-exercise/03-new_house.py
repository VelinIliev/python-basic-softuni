flowers_type = input()
number_of_flowers = int(input())
budjet = int(input())

roses_price = 5
dahlias_price = 3.8
tulips_price = 2.8
narcissus_price = 3
gladiolus_price = 2.5

if flowers_type == "Roses":
    total = number_of_flowers * roses_price
    if number_of_flowers > 80:
        total = total * .9
elif flowers_type == "Dahlias":
    total = number_of_flowers * dahlias_price
    if number_of_flowers > 90:
        total = total * .85
elif flowers_type == "Tulips":
    total = number_of_flowers * tulips_price
    if number_of_flowers > 80:
        total = total * .85
elif flowers_type == "Narcissus":
    total = number_of_flowers * narcissus_price
    if number_of_flowers < 120:
        total = total * 1.15
elif flowers_type == "Gladiolus":
    total = number_of_flowers * gladiolus_price
    if number_of_flowers < 80:
        total = total * 1.20

if budjet >= total:
    remaining_money = round(budjet - total,2)
    print(f'Hey, you have a great garden with {number_of_flowers} {flowers_type} and {remaining_money:.2f} leva left.')
elif budjet < total:
    needed_money = round(total - budjet,2)
    print(f'Not enough money, you need {needed_money:.2f} leva more.')