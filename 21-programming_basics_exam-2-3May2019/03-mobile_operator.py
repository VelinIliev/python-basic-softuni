contract_term = input()
contract_type = input()
mobile_internet = input()
number_of_months = int(input())

contract_price = 0

if contract_term == "one":
    if contract_type == "Small":
        contract_price = 9.98
    elif contract_type == "Middle":
        contract_price = 18.99
    elif contract_type == "Large":
        contract_price = 25.98
    elif contract_type == "ExtraLarge":
        contract_price = 35.99
if contract_term == "two":
    if contract_type == "Small":
        contract_price = 8.58
    elif contract_type == "Middle":
        contract_price = 17.09
    elif contract_type == "Large":
        contract_price = 23.59
    elif contract_type == "ExtraLarge":
        contract_price = 31.79

if mobile_internet == "yes":
    if contract_price <= 10:
        contract_price += 5.50
    elif contract_price <= 30:
        contract_price += 4.35
    elif contract_price > 30:
        contract_price += 3.85

total = contract_price * number_of_months

if contract_term == "two":
    total -= total * 0.0375

print(f'{total:.2f} lv.')