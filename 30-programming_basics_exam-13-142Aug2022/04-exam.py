number_of_students = int(input())
top_students = 0
students_between_400_499 = 0
students_between_300_399 = 0
fail_students = 0
grades = 0

for student in range(number_of_students):
    grade = float(input())
    if grade >= 5.00:
        top_students += 1
        grades += grade
    elif grade >= 4.00:
        students_between_400_499 += 1
        grades += grade
    elif grade >= 3.00:
        students_between_300_399 += 1
        grades += grade
    else:
        fail_students += 1
        grades += grade

top_students_percent = top_students / number_of_students * 100
print(f'Top students: {top_students_percent:.2f}%')
students_between_400_499_percent = students_between_400_499 / number_of_students * 100
print(f'Between 4.00 and 4.99: {students_between_400_499_percent:.2f}%')
students_between_300_399_percent = students_between_300_399 / number_of_students * 100
print(f'Between 3.00 and 3.99: {students_between_300_399_percent:.2f}%')
fail_students_percent = fail_students / number_of_students * 100
print(f'Fail: {fail_students_percent:.2f}%')
average_grade = grades / number_of_students
print(f'Average: {average_grade:.2f}')
