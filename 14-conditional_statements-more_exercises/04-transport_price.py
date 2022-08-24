travel_km = int(input())
travel_interval = input()

lowest_price = 0

if travel_interval == "day":
    taxi_price = 0.7 + travel_km * .79
else:
    taxi_price = .7 + travel_km * .9

if travel_interval == "day" and travel_km < 20:
    taxi_price = 0.7 + travel_km * .79
    lowest_price = taxi_price
elif travel_interval == "day" and travel_km < 100:
    taxi_price = 0.7 + travel_km * .79
    bus_price = travel_km * 0.09
    lowest_price = bus_price
elif travel_interval == "day" and travel_km >= 100:
    taxi_price = 0.7 + travel_km * .79
    bus_price = travel_km * 0.09
    train_price = travel_km * 0.06
    lowest_price = train_price
elif travel_interval == "night" and travel_km < 20:
    taxi_price = 0.7 + travel_km * .90
    lowest_price = taxi_price
elif travel_interval == "night" and travel_km < 100:
    taxi_price = 0.7 + travel_km * .79
    bus_price = travel_km * 0.09
    lowest_price = bus_price
elif travel_interval == "night" and travel_km >= 100:
    taxi_price = 0.7 + travel_km * .79
    bus_price = travel_km * 0.09
    train_price = travel_km * 0.06
    lowest_price = train_price

print(f'{lowest_price:.2f}')