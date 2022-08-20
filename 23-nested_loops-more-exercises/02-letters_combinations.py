interval_start = input()
interval_end = input()
letter_to_miss = input()
# print(ord("a"))
counter = 0

for first_letter in range(ord(interval_start), ord(interval_end) + 1):
    if chr(first_letter) != letter_to_miss:
        for second_letter in range(ord(interval_start), ord(interval_end) + 1):
            if chr(second_letter) != letter_to_miss:
                for third_letter in range(ord(interval_start), ord(interval_end) + 1):
                    if chr(third_letter) != letter_to_miss:
                        print(f'{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}', end = " ")
                        counter += 1

print(counter)