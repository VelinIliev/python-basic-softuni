cake_width = int(input())
cake_height = int(input())

pieces = cake_height * cake_width

while pieces > 0:
    pieces_taken = input()

    if pieces_taken != "STOP":
        pieces_taken = int(pieces_taken)
        pieces -= pieces_taken

    if pieces <= 0:
        print(f'No more cake left! You need {abs(pieces)} pieces more.')

    if pieces_taken == "STOP":
        print(f'{pieces} pieces are left.')
        break