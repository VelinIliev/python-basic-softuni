junior_riders = int(input())
senior_riders = int(input())
track_type = input()

if track_type == "trail":
    total_from_riders = junior_riders * 5.50 + senior_riders * 7
elif track_type == "cross-country":
    total_from_riders = junior_riders * 8.00 + senior_riders * 9.50
    if junior_riders + senior_riders >= 50:
        total_from_riders = total_from_riders * .75
elif track_type == "downhill":
    total_from_riders = junior_riders * 12.25 + senior_riders * 13.75
elif track_type == "road":
    total_from_riders = junior_riders * 20.00 + senior_riders * 21.50

total = total_from_riders * .95

print(f'{total:.2f}')