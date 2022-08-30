money_needed = float(input())

money_collected = 0

while money_collected < money_needed:
    cocktail_name = input()
    if cocktail_name == "Party!":
        print(f'We need {money_needed - money_collected:.2f} leva more.')
        break
    number_of_cocktails = int(input())

    cocktail_price = len(cocktail_name)

    order = cocktail_price * number_of_cocktails

    if order % 2 != 0:
        order *= .75

    money_collected += order

    if money_collected >= money_needed:
        print(f'Target acquired.')
        break

print(f'Club income - {money_collected:.2f} leva.')