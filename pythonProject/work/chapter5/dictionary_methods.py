

months_dictionary = {1: "January", 2: "Febuary", 3: "march",
                     4: "April", 5: "May", 6: "June", 7: "July",
                     8: "August", 9: "September", 10: "October",
                     11: "November", 12: "December"}

print("The dictionary items are:")
print(months_dictionary.items())

print("\nThe dictionary keys are: ")
print(months_dictionary.keys())

print("\nThe dictionary values are: ")
print(months_dictionary.values())

print("\nusing for loop to get dictionary items:")

for key in months_dictionary.keys():
    print(f"months_dictionary  key {[key]} = {months_dictionary[key]}")