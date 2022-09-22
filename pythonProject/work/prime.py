user_input = int(input("Enter a number"))

added_number = 0
for i in range(user_input, 0, -1):
    if user_input % i == 0:
        added_number += 1
if added_number == 2:
    print("Number is prime")
else:
    print("Number is not prime")

