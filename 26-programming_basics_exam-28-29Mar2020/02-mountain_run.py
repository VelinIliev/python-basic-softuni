record_time = float(input())
distance = float(input())
george_time_for_1m = float(input())

delay = distance // 50 * 30

george_time = george_time_for_1m * distance + delay

if george_time < record_time:
    print(f'Yes! The new record is {george_time:.2f} seconds.')
else:
    difference = george_time - record_time
    print(f'No! He was {difference:.2f} seconds slower.')
