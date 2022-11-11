number_of_students = int(input())

students_info = {}

for _ in range(number_of_students):

    student, grade = input().split()

    if student not in students_info:

        students_info[student] = []

    students_info[student].append(float(grade))

for student, grades in students_info.items():

    grades_list = " ".join(str(f"{grade:.2f}") for grade in grades)

    average_grade = sum(grades) / len(grades)

    print(f"{student} -> {grades_list} (avg: {average_grade:.2f})")