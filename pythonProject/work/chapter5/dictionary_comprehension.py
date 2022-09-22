# dict comprehension
names = ["alex", "Beth", "caroline", "dave", "eleanor", "fredie"]
import random

student_score = {student: random.randint(1, 100) for student in names}
# dict comprehension
passed_students = {student: score for (student, score) in student_score.items() if score >= 60}
print(passed_students)

# how to convert a sentence into a list
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)

# converting Celcius to fahrenheit
weather_c = {"Monday": 12,
             "Tuesday": 14,
             "Wednesday": 15,
             "Thursday": 14,
             "Friday": 21,
             "Saturday": 22,
             "Sunday": 24
             }

weather_f = {day: (temp_c * 9 / 5 + 32) for (day, temp_c) in weather_c.items()}
print(weather_f)

# using pandas to create data frames in dictionary
