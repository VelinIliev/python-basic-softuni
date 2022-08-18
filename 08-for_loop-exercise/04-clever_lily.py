age_of_lilly = int(input())
price_of_washing_machine = float(input())
price_of_toys = int(input())

sum_of_money = 0
count_toys = 0
money_to_recive = 10

for birthday in range(1, age_of_lilly + 1):
    if birthday % 2 == 0:
        sum_of_money = sum_of_money + money_to_recive - 1
        money_to_recive += 10
    else:
        count_toys += 1

sum_for_toys = count_toys * price_of_toys

total = sum_of_money + sum_for_toys

if total >= price_of_washing_machine:
    print(f'Yes! {(total - price_of_washing_machine):.2f}')
else:
    print(f'No! {(price_of_washing_machine-total):.2f}')
