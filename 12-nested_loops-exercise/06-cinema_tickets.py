tickets_total = 0
total_student_tickets = 0
total_standart_tickets = 0
total_kid_tickets = 0


while True:
    name_of_movie = input()
    if name_of_movie == "Finish":
        print(f'Total tickets: {tickets_total}')
        print(f'{total_student_tickets/tickets_total*100:.2f}% student tickets.')
        print(f'{total_standart_tickets/tickets_total*100:.2f}% standard tickets.')
        print(f'{total_kid_tickets/tickets_total*100:.2f}% kids tickets.')
        break
    free_places = int(input())

    sold_tickets = 0
    sold_students_tickets = 0
    sold_standard_tickets = 0
    sold_kids_tickets = 0

    while free_places != sold_tickets:
        ticket_type = input()
        if ticket_type == "End":
            print(f'{name_of_movie} - {((sold_tickets / free_places) * 100):.2f}% full.')
            tickets_total += sold_tickets
            total_student_tickets += sold_students_tickets
            total_standart_tickets += sold_standard_tickets
            total_kid_tickets += sold_kids_tickets
            break
        elif ticket_type == 'student':
            sold_tickets += 1
            sold_students_tickets += 1
        elif ticket_type == 'standard':
            sold_tickets += 1
            sold_standard_tickets += 1
        elif ticket_type == 'kid':
            sold_tickets += 1
            sold_kids_tickets += 1

        if free_places == sold_tickets:
            tickets_total += sold_tickets
            print(f'{name_of_movie} - {((sold_tickets / free_places) * 100):.2f}% full.')
            total_student_tickets += sold_students_tickets
            total_standart_tickets += sold_standard_tickets
            total_kid_tickets += sold_kids_tickets
