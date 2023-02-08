class Person:
    def __init__(self, name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def change_name(self, new_name):
        self.name = new_name

    def change_age(self, new_age):
        self.age = new_age

    def print_info(self):
        print(f"This is {self.name} they are {self.age} years old")