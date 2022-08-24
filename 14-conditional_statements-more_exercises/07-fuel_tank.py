type_of_fuel = input()
litres_in_tank = float(input())

if type_of_fuel == "Diesel" or type_of_fuel == "Gasoline" or type_of_fuel == "Gas":
    if litres_in_tank >= 25:
        print(f'You have enough {type_of_fuel.lower()}.')
    elif litres_in_tank < 25:
        print(f'Fill your tank with {type_of_fuel.lower()}!')
else:
    print(f'Invalid fuel!')