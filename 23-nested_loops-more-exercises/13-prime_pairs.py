first_number_start = int(input())
second_number_start = int(input())
first_number_end = first_number_start + int(input())
second_number_end = second_number_start + int(input())


def is_prime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


for first_number in range(first_number_start, first_number_end + 1):
    for second_number in range(second_number_start, second_number_end + 1):
        if is_prime(first_number) and is_prime(second_number):
            print(f'{first_number}{second_number}')



