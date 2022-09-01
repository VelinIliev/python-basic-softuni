movie_name = input()
number_of_days = int(input())
number_of_tickets = int(input())
ticket_price = float(input())
percent_for_cinema = int(input())

profit_per_day = number_of_tickets * ticket_price
total_profit = profit_per_day * number_of_days
total_profit_without_cinema = total_profit - total_profit * percent_for_cinema / 100

print(f'The profit from the movie {movie_name} is {total_profit_without_cinema:.2f} lv.')
