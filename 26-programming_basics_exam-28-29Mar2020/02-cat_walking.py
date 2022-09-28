walk_minutes = int(input())
number_of_walks = int(input())
calories_consumed = int(input())

calories_burned = number_of_walks * walk_minutes * 5

if calories_burned >= calories_consumed / 2:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.')