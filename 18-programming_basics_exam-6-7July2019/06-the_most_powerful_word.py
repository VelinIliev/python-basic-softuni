max_points = 0
winning_word = ""

# print(ord("I"))
# print(chr(97)
letters = ["a", "e", "o", "i", "u", "y", "A", "E", "O", "I", "U", "Y"]

while True:
    word = input()

    if word == "End of words":
        print(f'The most powerful word is {winning_word} - {max_points}')
        break

    sum_of_word = 0
    first_letter = ""

    for count, letter in enumerate(word):
        if count == 0:
            first_letter = letter
        sum_of_word += ord(letter)

    if first_letter in letters:
        sum_of_word = sum_of_word * len(word)
    else:
        sum_of_word = int(sum_of_word / len(word))

    if sum_of_word > max_points:
        max_points = sum_of_word
        winning_word = word