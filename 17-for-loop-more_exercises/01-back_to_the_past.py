inherited_money = float(input())
year_till_he_live = int(input())
age = 18

for year in range(1800, year_till_he_live + 1):
    if year % 2 == 0:
        inherited_money -= 12000
    else:
        inherited_money -= 12000 + 50 * age
    age += 1

if inherited_money >= 0:
    print(f'Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.')
else:
    print(f'He will need {abs(inherited_money):.2f} dollars to survive.')