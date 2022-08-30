town_name = input()
packet_type = input()
vip_discount = input()
days_of_vacation = int(input())

price_per_day = 0

if town_name == "Bansko" or town_name == "Borovets":
    if packet_type == "withEquipment":
        price_per_day = 100
        if vip_discount == "yes":
            price_per_day *= .9
    elif packet_type == "noEquipment":
        price_per_day = 80
        if vip_discount == "yes":
            price_per_day *= .95
elif town_name == "Varna" or town_name == "Burgas":
    if packet_type == "withBreakfast":
        price_per_day = 130
        if vip_discount == "yes":
            price_per_day *= .88
    elif packet_type == "noBreakfast":
        price_per_day = 100
        if vip_discount == "yes":
            price_per_day *= .93

if days_of_vacation > 7:
    days_of_vacation -= 1

if days_of_vacation < 1:
    print("Days must be positive number!")
elif town_name != "Bansko" and town_name != "Borovets" and town_name != "Varna" and town_name != "Burgas":
    print("Invalid input!")
elif packet_type != "withEquipment" and packet_type != "noEquipment" and packet_type != "withBreakfast" and packet_type != "noBreakfast":
    print("Invalid input!")
else:
    print(f"The price is {price_per_day * days_of_vacation:.2f}lv! Have a nice time!")