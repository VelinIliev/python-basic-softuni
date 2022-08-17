exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

exam_time = exam_hour * 60 + exam_min
arrival_time = arrival_hour * 60 + arrival_min

compare = exam_time - arrival_time

if compare < 0:
    print("Late")
elif compare >= 0 and compare <= 30:
    print("On time")
elif compare > 30:
    print("Early")
if compare > 0 and compare < 60:
    print(f'{compare} minutes before the start')
elif compare >= 60:
    compare_hours = compare // 60
    compare_min = compare % 60
    print(f'{compare_hours}:{compare_min:02d} hours before the start')
elif compare < 0 and compare > -60:
    compare = compare * -1
    print(f'{compare} minutes after the start')
elif compare <= -60:
    compare = compare * -1
    compare_hours = compare // 60
    compare_min = compare % 60
    print(f'{compare_hours}:{compare_min:02d} hours after the start')
