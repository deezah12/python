# list in traditional way
num = [1, 2, 3, 4]
sq = []
for n in num:
    sq.append(n ** 2)
print(sq)

# list using comprehension
num = [1, 2, 3, 4, 5]
sq = [n ** 2 for n in num]
print(sq)

# traditional way of printing letters
n_letters = []
for letters in 'semicolon':
    n_letters.append(letters)
print(n_letters)

# using comprehension
n_letters = [letters for letters in 'semicolon']
print(n_letters)

# cars with s in list
cars = ['jaguar', 'land rover', 'tesla', 'toyota', 'tata']
new_list = []
for x in cars:
    if 's' in x:
        new_list.append(x)
print(new_list)

# using comprehension
cars = ['jaguar', 'land rover', 'tesla', 'toyota', 'tata']
new_list = [x for x in cars if 's' in x]
print(new_list)

# using comprehension
new_list = [x for x in range(1, 10) if x > 5]
print(new_list)

# list
h_letters = []
for letter in 'human':
    h_letters.append(letter)
print(h_letters)

# using comprehension
h_letters = [letter for letter in 'human']
print(h_letters)

# using comprehension
letters = ['kayode', 'deezah', 'derek', 'abdul']
n_letters = [x for x in letters if 'k' in x]
print(n_letters)

# using comprehension
new_list = [n * 2 for n in range(1, 5)]
print(new_list)

# using comprehension condition
names = ["alex", "Beth", "caroline", "dave", "eleanor", "fredie"]
new_list = [name for name in names if len(name) < 5]
print(new_list)

# comprehension
names = ["alex", "Beth", "caroline", "dave", "eleanor", "fredie"]
new_list = [name.upper() for name in names if len(name) > 5]
print(new_list)

# dict comprehension
names = ["alex", "Beth", "caroline", "dave", "eleanor", "fredie"]
import random

student_score = {student: random.randint(1, 100) for student in names}
print(student_score)
# dict comprehension
passed_students = {student:score for (student,score) in students_scores.items() if score >= 60}
