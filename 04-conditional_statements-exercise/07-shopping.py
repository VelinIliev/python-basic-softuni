budget = float(input())
number_of_video_cards = int(input())
number_of_processors = int(input())
number_of_rams = int(input())

video_card_price = 250
total_video_cards = video_card_price * number_of_video_cards

processor_price = total_video_cards * .35
total_processors = processor_price * number_of_processors

ram_price = total_video_cards * .10
total_rams = ram_price * number_of_rams

grand_total = total_video_cards + total_processors + total_rams

if number_of_video_cards > number_of_processors:
    grand_total *= .85

if budget >= grand_total:
    money_left = round(budget - grand_total,2)
    print(f'You have {money_left:.2f} leva left!')
else:
    money_needed = round(grand_total - budget ,2)
    print(f'Not enough money! You need {money_needed:.2f} leva more!')