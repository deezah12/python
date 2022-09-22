# import array as arr
#
# a = arr.array('i', [1, 2, 3])
# print("the array created is : ", end=" ")
#
# for i in range(0, 3):
#     print(a[i], end=" ")
# print()
#
# a.insert(4, 4)
# a.insert(5, 5)
#
# for i in a:
#     print(i, end=" ")
# print()
#
# b = arr.array('f', [0.2, 0.4, 0.5])
# print("the array created is: ", end=" ")
#
# for i in range(0, 3):
#     print(b[i], end=" ")
# print()
#
# b.append(0.6)
# for i in b:
#     print(b, end=" ")
# print()
# print(f"access element at index 2 is {a[4]}")
#
# # removing an element from an array
# from array import *
#
# arr = array('i', [1, 2, 3, 1, 5, ])
# print("Original array: " + str(arr))
# for i in range(0, 5):
#     print(arr[i], end=" ")
#
# print("\r")
# # using pop to remove element at 2nd position
# print(f"the poped element is : {arr.pop(2)}", end="")
#
# print("\r")
# print(f"remaining array: {str(arr)}")
#
# arr.remove(1)
# print(f"the arrays left after removing  are {arr}")
# for i in range(0, 3):
#     print(arr[i], end=" ")
#
# # slicing of an array
# from array import *
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# arry = array('i', lst)
# for i in arry:
#     print(i, end=" ")
#
# sliced_array = arry[3:8]
# print("\r")
# print(f"sliced elements in range 3-8: {sliced_array}")
#
# sliced_array = arry[5:]
# print("\r")
# print(f"slicing elements from 5th element till end:\n {sliced_array}")
#
# sliced_array = arry[:]
# print("\r")
# print(f"printing all elements using slicing operation:\n {sliced_array}")

from array import *
arr = array('i', [1, 2, 3, 1, 2, 5])

# searching elements in array
# print(f'arrays are{str(arr)}')
# print(f"index occurence of 2 is : {arr.index(2)}", end=" ")
# print("\r")
# print(f"index occurence of 3 i : {arr.index(3)}", end=" ")

# updating elements in array
print(f"Array before updation: {str(arr)}", end="")
print("\r")
arr[2] =8
print(f"Array after updation: {arr}")