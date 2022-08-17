hour = int(input())
day = input()

working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
working_hours = [10, 18]

if day in working_days and working_hours[0] <= hour <= working_hours[1]:
    print("open")
else:
    print("closed")