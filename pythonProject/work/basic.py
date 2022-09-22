# print("sorry, is this the {} minute {}?".format(5, 'argument'))
# print(f"sorry is this the {5} minute {'argument'}?")

# print("{:^4} is {:.2f} years old".format('bill', 25))

# for i in range(1, 11):
#     sym = '*' * i
#     print('{:10}'.format(sym))
#     print(f'{sym:10}')
#
# river = 'Mississippi'
# target = input('input a character to find')
# for index in range(len(river)):
#     if river[index] == target:
#         print("letter found at index: ", index)
#         break
# else:
#     print('letter', target, 'not found in', river)

# def add(first_number: int, second_number: int) -> int:
#     return first_number + second_number
#
# print(add(2,3))
#

# def get_digit(number, position):
#     '''return digit at position in number, counting from right'''
#     return number//(10 ** position)%10
#
# print(get_digit(3794, 2))
#
# def get_length(number):
#     return len(number)
#
# print(get_length(str(37567)))

import math


def get_length(number: int):
    return math.ceil(math.log10(number))


print(get_length(34567777))
    
