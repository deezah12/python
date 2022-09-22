class Human:
    def __init__(self, name="", age=0):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, name:str):
        print("Calling the setter")
        if name.islower():
            raise ValueError("name cannot be all lower case")
        self._name = name

    @name.deleter
    def delete(self):
        print("im deleting")
        del self._age

    @age.setter
    def age(self, age: int):
        print("Calling the age")
        self._age = age
        if age < 0:
            raise ValueError("age must not be less than zero")


person = Human()
person. name = "Hadiza"
person.age = 58
print(f"my name is {person.name} and im {person.age} years old")


person1 = Human()
person1.name = "Umar"

person1.age = 0  
print(f"my name is {person1.name} and im {person1.age} years old")

