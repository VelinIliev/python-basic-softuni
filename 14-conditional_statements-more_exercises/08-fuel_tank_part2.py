type_of_fuel = input()
fuel_needed = float(input())
club_card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = .93

if club_card == 'Yes':
    gasoline_price = gasoline_price - .18
    diesel_price = diesel_price - .12
    gas_price = gas_price - .08

if type_of_fuel == "Gasoline":
    total = gasoline_price * fuel_needed
elif type_of_fuel == "Diesel":
    total = diesel_price * fuel_needed
elif type_of_fuel == "Gas":
    total = gas_price * fuel_needed

if fuel_needed >= 20 and fuel_needed <= 25:
    total = total * .92
elif fuel_needed > 25:
    total = total * .9

print(f'{total:.2f} lv.')