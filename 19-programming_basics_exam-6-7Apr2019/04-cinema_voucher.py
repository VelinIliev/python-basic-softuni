voucher_value = int(input())
cinema_tickets = 0
others_purchases = 0

while voucher_value > 0:
    purchase_name = input()

    if purchase_name == "End":
        break

    if len(purchase_name) > 8:
        if (voucher_value - (ord(purchase_name[0]) + ord(purchase_name[1]))) < 0:
            break
        else:
            voucher_value -= ord(purchase_name[0]) + ord(purchase_name[1])
            cinema_tickets += 1
    elif len(purchase_name) <= 8:
        if (voucher_value - ord(purchase_name[0])) < 0:
            break
        else:
            voucher_value -= ord(purchase_name[0])
            others_purchases += 1

print(f'{cinema_tickets}')
print(f'{others_purchases}')