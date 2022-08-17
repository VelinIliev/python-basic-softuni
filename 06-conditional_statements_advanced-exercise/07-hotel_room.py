month = input()
number_of_overnights = int(input())

app_price = 0
studio_price = 0

if month == "May" or month == "October":
    studio_price = 50 * number_of_overnights
    app_price = 65 * number_of_overnights
    if number_of_overnights > 14:
        studio_price = studio_price * .7
    elif number_of_overnights > 7:
        studio_price = studio_price * .95
elif month == "June" or month == "September":
    studio_price = 75.20 * number_of_overnights
    app_price = 68.70 * number_of_overnights
    if number_of_overnights > 14:
        studio_price = studio_price * .8
elif month == "July" or month == "August":
    studio_price = 76 * number_of_overnights
    app_price = 77 * number_of_overnights

if number_of_overnights > 14:
    app_price = app_price * .9

print(f'Apartment: {app_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')