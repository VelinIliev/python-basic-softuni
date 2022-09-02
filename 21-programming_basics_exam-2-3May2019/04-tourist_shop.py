budget = float(input())
product_counter = 0
total = 0

while True:
    product_name = input()
    if product_name == "Stop":
        print(f'You bought {product_counter} products for {total:.2f} leva.')
        break
    product_counter += 1

    product_price = float(input())

    if product_counter % 3 == 0:
        product_price = product_price / 2

    if total + product_price > budget:
        print(f"You don't have enough money!")
        print(f"You need {total + product_price - budget:.2f} leva!")
        break

    total += product_price
