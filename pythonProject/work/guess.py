import random

guess_number = random.randint(0, 100)
count = 0
#print(guess_number)
while count < 3:
    number = int(input("Enter a number: "))
    if number > guess_number:
        print("the number is too high")
    elif number < guess_number:
        print("the number is too low")
    else:
        print("You are a Lucky Guesser")
        break

    count += 1
if number != guess_number:
    print("Maximum Trials Exceeded")
