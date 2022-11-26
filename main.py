import random
import re

class Person():

    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_first_name(self):
        return self.__first_name

    def __str__(self):
        return f"{self.__first_name}, {self.last_name}, {self.age}"

def validate_csv(file):
    regex = r"^[a-zA-z ÕõÄäÖöÜü]*$"
    results = []
    for line in file.readlines():
        data = line.split(",")
        if re.match(regex,data[0]) and re.match(regex, data[1]):
            if "\n" in data[2] and 0 <= int(data[2].strip()) <= 100:
                results.append(True)
                continue
        results.append(False)
    return bool(False not in results)

def data_from_csv_to_Person_instances(file):
    persons_list = []
    with file as f:
        keys = ["first_name", "last_name", "age"]
        for line in f.readlines():
            values = line.strip().split(",")
            dicty = {}
            for i in range(len(keys)):
                dicty[keys[i]] = values[i]
            persons_list.append(Person(**dicty))
    print(f"Added {len(persons_list)} persons form csv file.")
    return persons_list

def divide_persons_into_group(persons_list, max_persons):
    groups = []

    num_of_groups = len(persons_list) / max_persons \
        if len(persons_list) % max_persons == 0 \
        else (len(persons_list) // max_persons) + 1

    for i in range(int(num_of_groups)):
        lst = []

        for i in range(max_persons):
            if len(persons_list) % max_persons != 0 and i == 0:
                continue
            person = random.choice(persons_list)
            lst.append(person)
            persons_list.remove(person)

        groups.append(lst)
    return groups

def groups_to_csv(groups):
    for i in range(len(groups)):
        _out = open(f"Group {i+1}.csv", "w", encoding="utf-8")
        with _out as f:
            for person in groups[i]:
                f.write(f"{person}\n")


if __name__ == "__main__":

    csv_path = input("Path to CSV file >>> ")
    file = open(csv_path, "r", encoding="utf-8")
    persons_list = data_from_csv_to_Person_instances(file)
    max_persons = int(input("How many persons in each group? >>> "))
    groups = divide_persons_into_group(persons_list, max_persons)
    groups_to_csv(groups)








