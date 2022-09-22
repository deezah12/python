# numbers = [1, 1, 2, 3, 5, 6, 13, 21, 34, 55]
# new_list = [n**2 for n in numbers]
# print(new_list)
#
#
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
new_list = [n for n in numbers if n % 2 == 0]
print(new_list)
#
#
# with open("file1.txt") as file1:
#     file_1_data = file1.readlines()
#
#
# with open("file2.txt") as file2:
#     file_2_data = file2.readlines()
#
#     result = [int(num) for num in file_1_data if num in file_2_data]
#     print(result)

letters = ["Kayode", "debby", "hannah", "john", "hopeson"]
new_list = [n for n in letters if "jo" in n]
print(new_list)
