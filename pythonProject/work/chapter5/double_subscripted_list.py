def print_grades(grades):
    students = (len(grades))
    exams = len(grades[0])

    print("the list is: ")
    print("             ")

    for i in range(exams):
        print("[%d]" % i)

    for i in range(students):
        print("grades[%d  " % i)
        for j in range(exams):
            print(grades[i][j], " ")


def minimum(grades):
    low_score = 100
    for student_exams in grades:
        for score in student_exams:
            if score < low_score:
                low_score = score
    return low_score


def maximum(grades):
    high_score = 100
    for student_exams in grades:
        for score in student_exams:
            if score < high_score:
                high_score = score
    return high_score


def average(set_of_grades):
    total = 0.0
    for grade in set_of_grades:
        total += grade
    return total / len(set_of_grades)


grades = [[77, 68, 86, 73],
          [96, 87, 89, 81],
          [70, 90, 86, 81]]

print_grades(grades)
print(f"lowest grade: {minimum(grades)}")
print(f"highest grade: {maximum(grades)}")
print("\n")

for i in range(len(grades)):
    print(f"Average for student {i}, is {average(grades[i])}")