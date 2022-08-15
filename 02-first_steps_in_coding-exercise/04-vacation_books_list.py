book_pages = int(input())
pages_per_hour = int(input())
days = int(input())

hours_to_complete_book = int(book_pages/pages_per_hour)
days_to_complete_book = int(hours_to_complete_book/days)
print(days_to_complete_book)