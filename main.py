import random


class Person():

    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_first_name(self):
        return self.__first_name

    def __str__(self):
        return f"{self.__first_name}, {self.last_name}, {self.age}"

def data_from_csv_to_Person_instances(csv_path):
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
    print(f"Added {len(persons_list)} persons form csv file.")
    return persons_list



if __name__ == "__main__":

    csv_path = input("Path to CSV file >>> ")
    persons_list = data_from_csv_to_Person_instances(csv_path)
    max_persons = int(input("How many persons in each group? >>> "))

    def divide_persons_into_group(persons_list, max_persons):
        groups = []

        num_of_groups = len(persons_list) / max_persons \
            if len(persons_list) % max_persons == 0 \
            else (len(persons_list) // max_persons) + 1


        for i in range(int(num_of_groups)):
            lst = []
            if len(persons_list) % max_persons != 0 and len(persons_list) < (2*max_persons):
                max_persons = max_persons - 1

            for i in range(max_persons):
                try:
                    person = random.choice(persons_list)
                    lst.append(person)
                    persons_list.remove(person)
                except IndexError:
                    continue

            groups.append(lst)
        return groups

    for item in divide_persons_into_group(persons_list, max_persons):
        for i in item:
            print(i)
        print("--------------------")




