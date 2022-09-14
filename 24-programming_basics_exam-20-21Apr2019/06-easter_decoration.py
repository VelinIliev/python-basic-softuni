basket_price = 1.50
wreath_price = 3.80
chocolate_bunny_price = 7.00

number_of_clients = int(input())

total_money_spend = 0

for client in range(number_of_clients):
    client_items = 0
    client_money_spend = 0
    while True:
        purchase = input()

        if purchase == "Finish":
            if client_items % 2 == 0:
                client_money_spend *= .8
            print(f'You purchased {client_items} items for {client_money_spend:.2f} leva.')
            total_money_spend += client_money_spend
            break
        elif purchase == "basket":
            client_items += 1
            client_money_spend += basket_price
        elif purchase == "wreath":
            client_items += 1
            client_money_spend += wreath_price
        elif purchase == "chocolate bunny":
            client_items += 1
            client_money_spend += chocolate_bunny_price

average_bill = total_money_spend / number_of_clients
print(f'Average bill per client is: {average_bill:.2f} leva.')