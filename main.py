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


def validate_data(line):
    """
    :param line: Line of text from CSV file.
    :return: True if valid, else False.
    """
    regex = r"^[a-zA-z ÕõÄäÖöÜü]*$"
    data = line.split(",")
    if len(data) == 3:
        if re.match(regex, data[0]) and re.match(regex, data[1]):
            if "\n" in data[2] and 0 <= int(data[2].strip()) <= 100:
                return True
    return False


def validate_csv(path):
    """
    :param path: Path to a CSV file.
    :return: True if all entries in CSV are valid, else False.
    """
    file = open(path, "r", encoding="utf-8")
    results = []
    for line in file.readlines():
        if validate_data(line):
            results.append(True)
            continue
        results.append(False)
    return bool(False not in results)


def read_data_from_csv(path):
    """
    :param path: Path to a CSV file.
    :return: A list of all the entries (as elements) from a CSV file.
    """
    file = open(path, "r", encoding="utf-8")
    with file:
        return file.readlines()



def create_instances(data):
    """
    :param data: List of all the entries from CSV file.
    :comment: Creates Person instances out of the data.
    :return: List of Person class instances.
    """
    list_of_persons = []
    keys = ["first_name", "last_name", "age"]
    for item in data:
        values = item.strip().split(",")
        param = {}
        for i in range(len(keys)):
            param[keys[i]] = values[i]
        list_of_persons.append(Person(**param))
    print(f"Added {len(list_of_persons)} persons form csv file.")
    return list_of_persons


def calculate_groups(list_of_persons, max_persons):
    """
    :param list_of_persons: List of Person class instances.
    :param max_persons: Maximum persons allowed per group (input).
    :return: An integer of how many groups to make.
    """
    num_of_groups = len(list_of_persons) / max_persons \
        if len(list_of_persons) % max_persons == 0 \
        else (len(list_of_persons) // max_persons) + 1
    return int(num_of_groups)


def divide_persons(list_of_persons, max_persons):
    """
    :param list_of_persons: List of Person class instances.
    :param max_persons: Maximum persons allowed per group (input).
    :return: Group of persons as a list (amount of people are equal to max_persons
    or max_persons - 1 if there will be reminder after dividing
    max_persons from total amount of persons (list_of_persons)
    """
    list_out = []
    for i in range(max_persons):
        if len(list_of_persons) % max_persons != 0 and i == 0:
            continue
        person = random.choice(list_of_persons)
        list_out.append(person)
        list_of_persons.remove(person)
    return list_out


def make_groups(num_of_groups, list_of_persons, max_persons):
    """
    :param num_of_groups: An integer of how many groups to make.
    :param list_of_persons: list_of_persons: List of Person class instances.
    :param max_persons: Maximum persons allowed per group (input).
    :return: Groups of persons as a list (nested list).
    """
    groups = []
    for i in range(num_of_groups):
        group = divide_persons(list_of_persons, max_persons)
        groups.append(group)
    return groups


def write_groups_to_csv(list_of_groups):
    """
    :param list_of_groups: Groups of persons as a list (nested list).
    :return: None. Writes each group from list_of_groups to a separate CSV file.
    """
    groups = list_of_groups
    for i in range(len(groups)):
        _out = open(f"Group {i+1}.csv", "w", encoding="utf-8")
        with _out as f:
            for person in groups[i]:
                f.write(f"{person}\n")


def main(path):
    data = read_data_from_csv(path)
    list_of_persons = create_instances(data)
    max_persons = int(input("Max amount of persons in a group >>> "))
    if max_persons < 1:
        raise ZeroDivisionError
    number_of_groups = calculate_groups(list_of_persons, max_persons)
    groups = make_groups(number_of_groups, list_of_persons, max_persons)
    write_groups_to_csv(groups)




if __name__ == "__main__":
    while True:
        csv_path = input("Path to CSV file >>> ")
        try:
            if validate_csv(csv_path):
                main(csv_path)
                break
            else:
                "Data in csv is incorrect!"
        except FileNotFoundError:
            print(f"No such file or directory: '{csv_path}'!")
            print("--------------------------------------------------")
        except ValueError:
            print("Max persons must be a number!")
            print("--------------------------------------------------")
        except IndexError:
            print("Max persons can't be greater then total amount of persons!")
            print("--------------------------------------------------")
        except ZeroDivisionError:
            print("Max persons must be greater then 0!")
            print("--------------------------------------------------")






