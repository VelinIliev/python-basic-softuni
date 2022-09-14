flour_per_kg_price = float(input())
number_of_kg_flour = float(input())
number_of_kg_sugar = float(input())
number_of_peel_eggs = int(input())
number_of_yeast = int(input())

total_flour = number_of_kg_flour * flour_per_kg_price

sugar_per_kg_price = flour_per_kg_price * .75
total_sugar = number_of_kg_sugar * sugar_per_kg_price

peel_of_eggs_price = flour_per_kg_price * 1.1
total_eggs = number_of_peel_eggs * peel_of_eggs_price

yeast_price = sugar_per_kg_price * .2
total_yeast = number_of_yeast * yeast_price

total = total_flour + total_sugar + total_eggs + total_yeast

print(f'{total:.2f}')