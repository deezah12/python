import one as one

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)

letters = ['kayode', 'deezah', 'derek', 'abdul']
n_letters = [len(x) for x in letters if 'k' in x]
print(n_letters)


#
# numbers = [1, 2, 3, 1, 2, 3, 2, 1, 4, 5]
# new_numbers = {num: len(num) for num in numbers}
# print(new_numbers)


def counter(iterable: list | str | tuple) -> dict:
    item_dict = {}
    from collections import Counter
    #
    # for item in iterable:
    #     if item in item_dict:
    #         item_dict[item] += 1
    #     else:
    #         item_dict[item] = 1
    # for item in iterable:
    #     # item_dict[item] = item_dict.get(item, 0) + 1
    #     item_dict[item] = iterable.count(item)
    # return item_dict

    return dict(Counter(iterable))


print(counter("hello deezah"))

lst = [num ** 2 for num in range(1, 11)]
print(lst)

# lst of odd numbers using list_comp

lst = [i for i in range(1, 11) if i % 2 != 0]
lst1 = [i for i in range(1, 11) if i % 2 == 0]
print(lst1)
print(lst)

a_dictionary = {1: 'one',
                2: 'two',
                3: 'three',
                4: 'four',
                5: 'five',
                6: 'six',
                7: 'seven',
                8: 'eight',
                9: 'nine',
                10: 'ten'
                }
a_list = [a_dictionary[i] for i in a_dictionary if i % 2 == 0]
print(a_list)

names = ["alex", "Beth", "Caroline", "dave", "Eleanor", "fredie"]
new_list = [name for name in names if name.istitle()]
print(new_list)

# with user input comprehension
# new_item = [input(f"{i + 1}. Name? ") for i in range(5)]
# print(new_item)
#
# # with an indefinite range
# number_of_times = int(input('how many names will you like to enter? '))
# new_item = [input(f"{i + 1}. Name? ") for i in range(number_of_times)]
# print(new_item)
#
# # with an indefinite range with a condition aves only the ones that passed the condition test
# number_of_times = int(input('how many names will you like to enter? '))
# new_item = [input(f"{i + 1}. Name? ") for i in range(number_of_times) if i.istitle()]
# print(new_item)

# evens = [i for i in range(1, 11) if i % 2 == 0]
# print(evens)

even_Squared_odd_cube = [number ** 2 if number % 2 == 0 else number ** 3 for number in range(1, 11)]
print(even_Squared_odd_cube)

