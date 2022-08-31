number_of_movies = int(input())

max_rating = 0
movie_wit_max_rating = ""

min_rating = 11
movie_with_min_rating = ""
total_ratings = 0

for movie in range(number_of_movies):
    movie_name = input()
    movie_rating = float(input())
    total_ratings += movie_rating
    if movie_rating > max_rating:
        max_rating = movie_rating
        movie_wit_max_rating = movie_name
    if movie_rating < min_rating:
        min_rating = movie_rating
        movie_with_min_rating = movie_name

print(f'{movie_wit_max_rating} is with highest rating: {max_rating}')
print(f'{movie_with_min_rating} is with lowest rating: {min_rating}')
print(f'Average rating: {total_ratings / number_of_movies:.1f}')