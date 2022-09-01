hall_capacity = int(input())
ticket_price = 5
total_income = 0
total_people_entered = 0

while True:
    people_entered = input()
    if people_entered == "Movie time!":
        print(f'There are {hall_capacity - total_people_entered} seats left in the cinema.')
        break
    else:
        people_entered = int(people_entered)
    if total_people_entered + people_entered > hall_capacity:
        print(f'The cinema is full.')
        break

    current_bill = people_entered * ticket_price

    if people_entered % 3 == 0:
        current_bill -= 5
    total_people_entered += people_entered
    total_income += current_bill

print(f'Cinema income - {round(total_income)} lv.')