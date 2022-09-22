 # user_input = int(input("Enter a number"))
# value = range(1, 13)
#
# for x in value :
#     result = user_input * x
#     print(user_input, "*", x, "=", result)

user_input = int(input("Enter a number"))
value = range(1, 13)
new_value = [x * range(1, 13) for x in value]
print(new_value)