price_for_baggage_over_20kg = float(input())
baggage_kilos = float(input())
days_till_trip = int(input())
number_of_baggage = int(input())

baggage_price = 0

if baggage_kilos < 10:
    baggage_price = price_for_baggage_over_20kg * .2
elif baggage_kilos <= 20:
    baggage_price = price_for_baggage_over_20kg * .5
elif baggage_kilos > 20:
    baggage_price = price_for_baggage_over_20kg

if days_till_trip > 30:
    baggage_price *= 1.1
elif days_till_trip >= 7:
    baggage_price *= 1.15
elif days_till_trip < 7:
    baggage_price *= 1.4

total = round(baggage_price * number_of_baggage,2)

print(f'The total price of bags is: {total:.2f} lv.')