
table1 = [[1, 2, 3], [4, 5, 6]]
table2 = ((1, 2), (3,), (4, 6, 5))

print("value in table1 by row are")
for row in table1:
    for item in row:
        print(item,)
    print()

print("Value in table2 by row are")
for row in table2:
    for item in row:
        print(item)
    print()