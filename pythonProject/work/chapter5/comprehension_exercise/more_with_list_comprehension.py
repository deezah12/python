# 1. def odd_or_zero(num):
#     if num % 2 == 0:
#         return 0
#     else:
#         return num
#
#
# a_list = range(1, 11)
# a_lists = [odd_or_zero(i) for i in a_list]
# print(a_lists)
#
# 2. string = input("Enter a number: ")
# a_dictionary = {1: 'one',
#                 2: 'two',
#                 3: 'three',
#                 4: 'four',
#                 5: 'five',
#                 6: 'six',
#                 7: 'seven',
#                 8: 'eight',
#                 9: 'nine',
#                 0: 'zero'
#                 }
# items = [a_dictionary[int(number)] for number in string]
# # '-'.join(items)
# print(items)
#
# 3. avengers = ["Iron Man", "Captain America", "Thor",
#             "The Incredible Hulk", "Bla avengers ck Widow", "Hawkeye"]
#
# avenge = [i for i in avengers if len(i) >= 8]
# print(avenge)
#
# 4. numbers = list(range(50, 150, 5))
# lst = [n for n in numbers if n % 2 == 0 and n > 100]
# print(lst)

# 5. str = "Fall is Awesome in Alabama"
# lst = ["%" + n + "%" for n in str.split()]
# print(lst)

# 6. my_lst = [i for i in range(1, 101) if i % 2 == 0]
# print(my_lst)

# 7. word_list = ["this", "is", "an", "example"]
# new_word_list = [i[0] for i in word_list]
# print(new_word_list)

# 8.msg = 'happy birthday!'
# lst = [m for m in msg if m != " " and m != "!"]
# print(lst)

# 9. string = ['one', 'seven', 'three', 'two', 'ten']
# lst = [(len(str), str.upper()) for str in string if len(str) > 3]
# print(lst)

# 10.names = ["Jules Verne", "Alexandre Dumas", "Maurice Dru-on"]
# lst = [n.split()[0] + ',' + n.split()[1] for n in names]
# print(lst)

# 11.x_and_y = [(x, y) for x in range(1, 6) for y in range(1, 6)]
# print(x_and_y)

# 12. lst = [12, 24, 35, 70, 88, 120, 155]
# new_lst = [value for index, value in enumerate(lst) if index != 0 and index != 2
#            and index != 4 and index != 6]
# print(new_lst)

prairie_pirates = [
    ['Tractor Jack', 1000, True],
    ['Plowshare Pete', 950, False],
    ['Prairie Lily', 245, True],
    ['Red River Rosie', 350, True],
    ['Mad Athabasca McArthur', 842, False],
    ['Assiniboine Sally', 620, True],
    ['Thresher Tom', 150, True],
    ['Cranky Canola Carl', 499, False]
]
best_plunderers = [pirate[0] for pirate in prairie_pirates if pirate[1] > 400]
print(best_plunderers)

like_plunderers = [pirate[0] for pirate in prairie_pirates if pirate[2] != True]
print(like_plunderers)
