sector_end = input()
number_of_rows = int(input())
number_of_seats_on_odd_row = int(input())
number_of_seats_on_even_row = number_of_seats_on_odd_row + 2
number_of_seats = 0

for sector in range(ord('A'), ord(sector_end) + 1):
    for row in range(1, number_of_rows + 1):
        if row % 2 != 0:
            for seat in range(1, number_of_seats_on_odd_row + 1):
                print(f'{chr(sector)}{row}{chr(seat+96)}')
                number_of_seats += 1
        else:
            for seat in range(1, number_of_seats_on_even_row + 1):
                print(f'{chr(sector)}{row}{chr(seat+96)}')
                number_of_seats += 1
    number_of_rows += 1
print(number_of_seats)