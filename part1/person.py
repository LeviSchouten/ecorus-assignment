class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def happy_birthday(self):
        self.age += 1

    def change_name(self, name):
        self.name = name
