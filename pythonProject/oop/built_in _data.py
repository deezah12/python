class CustomDict(dict):

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("Can only take a string key")
        super().__setitem__(key, value)

    def __getitem__(self, key):
        if not isinstance(key, str):
            raise TypeError("Can only take a string key")
        super().__getitem__(key)


m = CustomDict()
m["1"] = 6
print(m)


class CustomList(list):
    def __setitem__(self, index, value):
        if index < 0:
            raise ValueError("index must not be negative or less than zero")
        super().__setitem__(index, value)

    def __getitem__(self, index):
        if index < 0:
            raise ValueError("index must not be negative or less than zero")
        super().__getitem__(index)

