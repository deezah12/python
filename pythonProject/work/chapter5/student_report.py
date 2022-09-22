
students_list = []
numbers = int(input("Enter number of students :"))
subjects = int(input("Enter number of subjects: "))

subjects_details = [input("Enter subject names") for i in range(subjects)]

for i in range(numbers):
    students_name = input("Enter names of student :")
    subject_scores = []
    for k in range(subjects):
        mark = float(input(f"Enter marks for {subjects_details[k]} :"))
        marks = {"sub": subjects_details[k], "score": mark}
        subject_scores.append(marks)

    stud = {"name": students_name, "subject_scores": subject_scores}
    students_list.append(stud)
print("list  of all students created :")
for el in students_list:
    score = el["subject_scores"]
    for i in score:
        a_score = i["score"]
    print(el)


def get_total_score():
    sc_ = 0
    new_arr = []
    for student in students_list:
        for i in range(len(student['subject_scores'])):
            sc_ += student['subject_scores'][i]["score"]
        new_arr.append(sc_)
    return new_arr


print(get_total_score())

