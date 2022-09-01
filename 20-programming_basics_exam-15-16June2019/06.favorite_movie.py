movie_counter = 0
best_movie_score = 0
best_movie_name = ""

while True:
    movie_name = input()
    movie_counter += 1

    if movie_name == "STOP":
        break

    current_movie_score = 0

    for letter in movie_name:
        if 65 <= ord(letter) <= 90:
            points = ord(letter) - len(movie_name)
            current_movie_score += points
        elif 97 <= ord(letter) <= 122:
            points = ord(letter) - 2 * len(movie_name)
            current_movie_score += points
        else:
            points = ord(letter)
            current_movie_score += points

    if movie_counter == 7:
        print("The limit is reached.")
        break

    if current_movie_score > best_movie_score:
        best_movie_score = current_movie_score
        best_movie_name = movie_name

print(f'The best movie for you is {best_movie_name} with {best_movie_score} ASCII sum.')

# print(ord("a"))
# print(ord("z"))
