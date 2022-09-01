budget = float(input())
number_of_series = int(input())

total = 0

for series in range(number_of_series):
    name_of_series = input()
    price_for_series = float(input())
    if name_of_series == "Thrones":
        price_for_series *= .5
    elif name_of_series == "Lucifer":
        price_for_series *= .6
    elif name_of_series == "Protector":
        price_for_series *= .7
    elif name_of_series == "TotalDrama":
        price_for_series *= .8
    elif name_of_series == "Area":
        price_for_series *= .9
    total += price_for_series

if budget >= total:
    print(f'You bought all the series and left with {budget - total:.2f} lv.')
else:
    print(f'You need {total - budget:.2f} lv. more to buy the series!')