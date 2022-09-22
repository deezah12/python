class CustomClass:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return "multiplication"

    def __lt__(self, other):
        return self.num < other.num

    def __str__(self):
        return str(self.num)

    def __repr__(self) -> str:
        return str(self.num)


c1 = CustomClass(1)
c2 = CustomClass(2)

print(c1 + c2)
print(c1 * c2)
print(c1 < c2)

lst = [c2, c1]
print(c1)
lst.sort()
print(lst)

import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        return f"{self.x}i + {self.y}j"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __len__(self):
        return 1

    def __lt__(self, other):
        return abs(self) < abs(other)


v1 = Vector(2, 4)
v2 = Vector(1, 6)

print(v1)

v3 = v1 +v2
print(v3)
lst = [v3,v1,v2]
lst.sort()
print(lst)
