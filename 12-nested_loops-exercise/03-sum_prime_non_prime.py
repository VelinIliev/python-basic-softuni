sum_of_prime_numbers = 0
sum_of_non_prime_numbers = 0

def is_prime(number):
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number < 2:
        return False
    for n in range(3, int(number ** 0.5) + 1, 2):
        if number % n == 0:
            return False
    return True

while True:
    number = input()

    if number != "stop":
        number = int(number)
        if number < 0:
            print("Number is negative.")
        elif is_prime(number):
            sum_of_prime_numbers += number
        else:
            sum_of_non_prime_numbers += number
    else:
        print(f'Sum of all prime numbers is: {sum_of_prime_numbers}')
        print(f'Sum of all non prime numbers is: {sum_of_non_prime_numbers}')
        break

