sum_needed = int(input())

transaction_counter = 0
total_sold_credit_card = 0
total_sold_cash = 0
total_sold = 0
cash_count = 0
credit_card_count = 0

while total_sold < sum_needed:
    transaction_counter += 1
    amount = input()
    if amount == "End":
        print("Failed to collect required money for charity.")
        break
    else:
        amount = int(amount)

    if transaction_counter % 2 == 0:
        type = "credit card"
    else:
        type = "cash"
    if amount > 100 and type == "cash":
        print("Error in transaction!")
    elif amount < 10 and type == "credit card":
        print("Error in transaction!")
    elif type == 'credit card':
        total_sold += amount
        total_sold_credit_card += amount
        credit_card_count += 1
        print("Product sold!")
    elif type == "cash":
        total_sold += amount
        total_sold_cash += amount
        cash_count += 1
        print("Product sold!")

    if total_sold >= sum_needed:
        print(f'Average CS: {total_sold_cash/cash_count:.2f}')
        print(f'Average CC: {total_sold_credit_card/credit_card_count:.2f}')