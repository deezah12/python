class Human:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    def __str__(self):
        return f"name={self.last_name} {self.first_name}, age= {self.age}"

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.first_name}', '{self.last_name}', '{self.age}')"


class Manager(Human):
    def __init__(self, first_name, last_name, age, bonus: float):
        self.bonus = bonus
        super().__init__(first_name, last_name, age)

    def full_name(self):
        return f"{self.last_name[0].upper()}. {self.first_name}"

    def pay_salary(self, salary):
        return salary + self.bonus


class Employee(Human):

    def pay_salary(self, salary):
        return salary


employee1 = Employee("hadiza", "Umar", 23)
# manager1 = Manager("Emma", "Cappy", 43, "male")
# print(manager1.full_name())
# print(employee1.full_name())
print(employee1)
print(f"{employee1!r}")
#
# human_list = [employee1, manager1, Human("sapien", "Homo", 0, "unknown")]
# for human in human_list:
#     print(human.full_name())
