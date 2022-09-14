number_of_easter_breads = int(input())
number_of_dozen_eggs = int(input())
number_of_cookies_kilos = int(input())

easter_bred_price = 3.2
eggs_12_price = 4.35
cookies_per_kg_price = 5.40
egg_paint_per_egg = .15

total_easter_bred = number_of_easter_breads * easter_bred_price
total_eggs = number_of_dozen_eggs * eggs_12_price
total_cookies = number_of_cookies_kilos * cookies_per_kg_price
total_paint = number_of_dozen_eggs * 12 * egg_paint_per_egg

total = total_easter_bred + total_eggs + total_cookies + total_paint

print(f'{total:.2f}')