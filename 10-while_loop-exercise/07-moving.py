free_space_width = int(input())
free_space_heigh = int(input())
free_space_length = int(input())

total_free_space = free_space_heigh * free_space_width * free_space_length

while total_free_space > 0:
    number_of_boxes = input()

    if number_of_boxes != "Done":
        number_of_boxes = int(number_of_boxes)
        total_free_space -= number_of_boxes

    if total_free_space < 0:
        print(f'No more free space! You need {abs(total_free_space)} Cubic meters more.')

    if number_of_boxes == "Done":
        print(f'{total_free_space} Cubic meters left.')
        break
