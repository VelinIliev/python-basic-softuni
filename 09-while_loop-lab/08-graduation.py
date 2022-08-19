name = input()

class_no = 0
excluded = 0
grades = 0

while True:
    grade = float(input())
    class_no += 1

    if grade < 4:
        excluded += 1
        if excluded == 2:
            print(f"{name} has been excluded at {class_no} grade")
            break
        class_no -= 1
    else:
        grades += grade

    if class_no == 12:
        average_grade = grades / class_no
        print(f'{name} graduated. Average grade: {average_grade:.2f}')
        break


