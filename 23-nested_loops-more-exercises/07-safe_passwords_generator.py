a = int(input())
b = int(input())
max_number_of_password = int(input())
passwords_count = 0

for A in range(35, 56):
    if passwords_count == max_number_of_password:
        break
    for B in range(64, 97):
        if passwords_count == max_number_of_password:
            break
        for x in range(1, a + 1):
            if passwords_count == max_number_of_password:
                break
            for y in range(1, b + 1):
                if passwords_count == max_number_of_password:
                    break
                print(f'{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}', end = "|")
                A += 1
                if A > 55:
                    A = 35
                B += 1
                if B > 96:
                    B = 64
                passwords_count += 1

        break
    break
