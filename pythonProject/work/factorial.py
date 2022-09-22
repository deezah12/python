import math


def fact(n):
    return math.factorial(n)


number = int(input("Enter number: "))
value = fact(number)
print("factorial of", number, "is", value)
