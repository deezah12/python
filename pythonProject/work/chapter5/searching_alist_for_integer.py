alist = range(0, 199, 2)

search_key = int(input("Enter an integer search key: "))

if search_key in alist:
    print("search key found at index: ", alist.index(search_key))
else:
    print("value not found")