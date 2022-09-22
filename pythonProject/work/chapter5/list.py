# creating accessing and changing a list.

alist = []  # create the list

# add values to the list
for number in range(1, 11):
    alist += [number]
print(f"The value of a list is: {alist}")

# access list values by iteration
print("\nAcessing values by iteration:")

for item in alist:
    print(item)

# accessing lit values by index
print("\nAcessing values by index:")
print("index\tvalue")
for i in range(len(alist)):
    print(i,  alist[i])



