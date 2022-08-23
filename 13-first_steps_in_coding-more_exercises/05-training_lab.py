room_width = float(input()) * 100
room_height = float(input()) * 100 - 100

room_size = room_width * room_height

rows = int(room_height / 70)
columns = int(room_width / 120)
door = 1
teacher_desk = 2

total_study_places = rows * columns - door - teacher_desk

print(total_study_places)