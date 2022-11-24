

class Person():

    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_first_name(self):
        return self.__first_name

    def __str__(self):
        return f"{self.__first_name}, {self.last_name}, {self.age}"


if __name__ == "__main__":

    csv_path = input("Path to CSV file >>> ")
    file = open(csv_path, "r", encoding="utf-8")
    persons_list = []
    with file as f:
        keys = [i for i in f.readline().strip().split(",")]

        for line in f.readlines():
            values = [i for i in line.strip().split(",")]
            dicty = {}
            for i in range(len(keys)):
                dicty[keys[i]] = values[i]

            persons_list.append(Person(**dicty))
            
    for item in persons_list:
        print(item)



