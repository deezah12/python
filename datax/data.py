from dataclasses import dataclass, field, fields, make_dataclass


@dataclass(order=True)
class Person:
    name: str
    height: tuple = field(init=False)
    age: int = 0
    children: list = field(default_factory=lambda: [])

    def get_age(self):
        return self.age


p1 = Person("Hadi", 21)
p2 = Person("victor", 21)
# p1.hello = "me"
# print(p1.__dict__)
# print(p1.hello)

Human = make_dataclass("Human", ["name", "age"])
h1 = Human("Hadi", 23)
print(h1)
