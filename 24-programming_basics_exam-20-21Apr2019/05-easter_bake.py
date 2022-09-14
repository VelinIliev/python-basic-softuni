from math import ceil

number_of_easter_breads = int(input())

sugar_pack = 950
flour_pack = 750

sugar_needed = 0
flour_needed = 0

max_sugar = 0
max_flour = 0

for easter_bread in range(number_of_easter_breads):
    sugar = int(input())
    flour = int(input())

    sugar_needed += sugar
    flour_needed += flour

    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour

sugar_packs_needed = int(ceil(sugar_needed / sugar_pack))
flour_packs_needed = int(ceil(flour_needed / flour_pack))

print(f'Sugar: {sugar_packs_needed}')
print(f'Flour: {flour_packs_needed}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')