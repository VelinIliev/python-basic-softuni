time_for_filming = int(input())
number_of_scenes = int(input())
duration_of_scene = int(input())

preparation = time_for_filming * .15

total_time = preparation + number_of_scenes * duration_of_scene

if total_time <= time_for_filming:
    print(f'You managed to finish the movie on time! You have {round(time_for_filming - total_time)} minutes left!')
else:
    print(f'Time is up! To complete the movie you need {round(total_time - time_for_filming)} minutes.')