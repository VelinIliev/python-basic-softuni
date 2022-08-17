number_1 = int(input())
number_2 = int(input())
operator = input()

if operator == "+":
    sum = number_1 + number_2
    if sum % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f'{number_1} {operator} {number_2} = {sum} - {even_or_odd}')
elif operator == "-":
    substract = number_1 - number_2
    if substract % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f'{number_1} {operator} {number_2} = {substract} - {even_or_odd}')
elif operator == "*":
    multiply = number_1 * number_2
    if multiply % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f'{number_1} {operator} {number_2} = {multiply} - {even_or_odd}')
elif operator == "/":
    if number_2 == 0:
        print(f"Cannot divide {number_1} by zero")
    else:
        divide = number_1 / number_2
        print(f'{number_1} / {number_2} = {divide:.2f}')
elif operator == "%":
    if number_2 == 0:
        print(f"Cannot divide {number_1} by zero")
    else:
        modolus = number_1 % number_2
        print(f'{number_1} % {number_2} = {modolus}')