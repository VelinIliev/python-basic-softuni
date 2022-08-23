jury_members = int(input())
grades = []

while True:
    presentation_name = input()
    if presentation_name == "Finish":
        sum_grades = 0
        for grade in grades:
            sum_grades += grade
        average_score = sum_grades / len(grades)
        print(f"Student's final assessment is {average_score:.2f}.")
        break
    else:
        curent_score = 0
        for grade in range(jury_members):
            grade = float(input())
            grades.append(grade)
            curent_score += grade
        average_score = curent_score / jury_members
        print(f'{presentation_name} - {average_score:.2f}.')