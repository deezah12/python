from array import *


# 1.acessing first 3 index  elemnts in the array
# arr = array('i', [1, 3, 5, 7, 9])
# sliced = arr[0:3]
# print(f"sliced arrays are {sliced}")
# print("Access first three items individually")
# print(f"{arr[0]}")
# print(f"{arr[1]}")
# print(f"{arr[2]}")

# 2. appending item to the array
# arr = array("i", [1, 3, 5, 7, 9])
# arr.append(11)
# print(f"New array {arr}")

# 3. reversing an array
# arr = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
# print(f"original array {arr}")
# arr.reverse()
# print(f"the reversed array is {arr}")

# 4. length of bytes of each array element internally
# arr = array('i', [1, 3, 5, 7, 9])
# arr_length = len(arr)
# print(f"Length in bytes of one array item: {arr.itemsize} ")

# 5. Write a Python program to get the current memory address
# and the length in elements of the buffer used to hold an array's
# contents and also find the size of the memory buffer in bytes.

# arr = array('i', [1, 3, 5, 7, 9])
# print(f"Current memory address and the length in elements of the buffer:"
#       f"{arr.buffer_info()}")
# print(f"The size of the memorybuffer in bytes: "
#       f"{arr.buffer_info()[1]* arr.itemsize}")

# 6. Write a Python program to get the number
# of occurrences of a specified element in an array.

# arr = array('i', [1, 3, 5, 3, 7, 9, 3])
# occur = arr.count(3)
# print(f"the number of occurrence of 3 in the said array is: {occur}")

# 7.Write a Python program to append items from inerrable
# to the end of the array.

# arr = array('i', [1, 3, 5, 7, 9])
# print(f"original array: {arr}")
# arr.extend(arr)
# print(f"Extended array: {arr}")

# 8.  Write a Python program to convert an array to an array of
# machine values and return the bytes representation.

# arr = array('b', [72, 97, 100, 105, 122, 97, 109, 121, 108, 111, 118, 101])
# st = arr.tobytes()
# print(st)


# 9.  Write a Python program to append items from a specified list.
# lst = [1, 2, 3, -8]
# arr = array('i', [])
# print(f"Items in the list: {lst}")
# arr.fromlist(lst)
# print(f"Items in the array : {str(arr)}")

# 10. Write a Python program to insert a new item before
# the second element in an existing array.
# arr = array('i', [1, 3, 5, 7, 9])
# arr.insert(1, 4)
# print(f"New array: {arr}")

# 11.  Write a Python program to remove a specified
# item using the index from an array.
# arr = array('i', [1, 3, 5, 7, 9])
# arr.pop(2)
# print(f"New array: {arr}")

# 12. Write a Python program to remove the first occurrence of
# a specified element from an array.
# arr = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
# arr.remove(3)
# print(f"New array: {arr}")

# 13.Write a Python program to convert an
# array to an ordinary list with the same items.
# arr = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
# lst = arr.tolist()
# print(f"list {lst}")

# 14.  Write a Python program to find whether a given
# array of integers contains any duplicate element.
# Return true if any value appears at least twice in the said
# array and return false if every element is distinct.
#
# def duplicate_num(array_num):
#     num_set = set(array_num)
#     return len(array_num) != len(num_set)
#
#
# print(duplicate_num([1, 2, 3, 4]))
# print(duplicate_num([1, 2, 3, 4, 4, 5, 5]))

# 15.  Write a Python program to find the first duplicate
# element in a given array of integers.
# Return -1 If there are no such elements.

# def duplicate(num):
#     num_set = set()
#     no_duplicate = -1
#
#     for i in range(len(num)):
#         if num[i] in num_set:
#             return num[i]
#         else:
#             num_set.add(num[i])
#
#     return no_duplicate
#
#
# print(duplicate([1, 2, 3, 4, 5, 3, 4]))
# print(duplicate([1, 2, 3, 4]))

# 16. Write a Python program to check
# whether it follows the sequence given in the patterns array.

# def is_samePatterns(colors, patterns):
#     if len(colors) != len(patterns):
#         return False
#     cset = set()
#     pset = set()
#     sdict = {}
#     for i in range(len(patterns)):
#         pset.add(patterns[i])
#         cset.add(colors[i])
#         if patterns[i] not in sdict.keys():
#             sdict[patterns[i]] = []
#         keys = sdict[patterns[i]]
#         keys.append(colors[i])
#         sdict[patterns[i]] = keys
#     if len(pset) != len(cset):
#         return False
#     for values in sdict.values():
#         for i in range(len(values) - 1):
#             if values[i] != values[i + 1]:
#                 return False
#     return True
#
#
# print(is_samePatterns(['red', 'green', 'blue'], ['a', 'b', 'b']))


