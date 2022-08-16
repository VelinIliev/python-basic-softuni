world_record = float(input())
distance = float(input())
seconds_per_meter = float(input())

ivans_time = round(distance * seconds_per_meter + int(distance / 15) * 12.5, 2)

if ivans_time < world_record:
    print(f"Yes, he succeeded! The new world record is {ivans_time:.2f} seconds.")
else:
    seconds_left = round(ivans_time - world_record, 2)
    print(f'No, he failed! He was {seconds_left:.2f} seconds slower.')