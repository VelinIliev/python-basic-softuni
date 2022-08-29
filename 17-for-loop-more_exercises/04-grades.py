number_of_students = int(input())
top_students = 0
good_students = 0
middle_students = 0
fail_students = 0
grades = 0

for student in range(number_of_students):
    grade = float(input())
    grades += grade
    if grade >= 5:
        top_students += 1
    elif grade >= 4:
        good_students += 1
    elif grade >= 3:
        middle_students += 1
    else:
        fail_students += 1

print(f'Top students: {top_students / number_of_students * 100:.2f}%')
print(f'Between 4.00 and 4.99: {good_students / number_of_students * 100:.2f}%')
print(f'Between 3.00 and 3.99: {middle_students / number_of_students * 100:.2f}%')
print(f'Fail: {fail_students / number_of_students * 100:.2f}%')
print(f'Average: {grades / number_of_students:.2f}')