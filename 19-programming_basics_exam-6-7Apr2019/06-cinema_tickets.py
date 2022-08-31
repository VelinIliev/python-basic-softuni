student_tickets = 0
standard_tickets = 0
kid_tickets = 0

watching_movies = True

while watching_movies:
    movie_name = input()

    if movie_name == "Finish":
        total_tickets = student_tickets + standard_tickets + kid_tickets
        print(f'Total tickets: {total_tickets}')
        print(f'{student_tickets / total_tickets * 100:.2f}% student tickets.')
        print(f'{standard_tickets / total_tickets * 100:.2f}% standard tickets.')
        print(f'{kid_tickets / total_tickets * 100:.2f}% kids tickets.')
        watching_movies = False
        break

    free_places = int(input())
    sold_tickets = 0
    selling_tickets = True

    while selling_tickets:
        ticket_type = input()
        if ticket_type == "End":
            selling_tickets = False
        elif ticket_type == "standard":
            standard_tickets += 1
            sold_tickets += 1
        elif ticket_type == "student":
            student_tickets += 1
            sold_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
            sold_tickets += 1
        if sold_tickets >= free_places:
            selling_tickets = False
    print(f'{movie_name} - {sold_tickets / free_places * 100:.2f}% full.')



