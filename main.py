

class Person():

    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_first_name(self):
        return self.__first_name
