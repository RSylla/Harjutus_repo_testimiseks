import unittest
from main import validate_data, make_groups, calculate_groups


class TestCSV(unittest.TestCase):

    def setUp(self):
        self.list28persons = [person for person in range(1, 29)]
        self.list25persons = [person for person in range(1, 29)]

    def test_validate_csv_format(self):
        self.assertFalse(validate_data("30,Martin,Appo\n"))
        self.assertFalse(validate_data("Martin\n"))
        self.assertTrue(validate_data("Martin,Appo,30\n"))

    def test_validate_csv_entries(self):
        self.assertFalse(validate_data("M4rtin,App0,20\n"))
        self.assertFalse(validate_data("Martin,Appo,120\n"))
        self.assertTrue(validate_data("Appo,Martin,30\n"))

    def test_make_groups(self):
        max_persons = 5
        caseTrue = range(max_persons - 1, max_persons + 1)

        num_of_groups = calculate_groups(self.list28persons, max_persons)
        groups = make_groups(num_of_groups, self.list28persons, max_persons)
        for group in groups:
            self.assertTrue(len(group) in caseTrue)
        for group in groups:
            self.assertFalse(len(group) not in caseTrue)

        max_persons = 4
        num_of_groups = calculate_groups(self.list25persons, max_persons)
        groups = make_groups(num_of_groups, self.list25persons, max_persons)
        for group in groups:
            self.assertTrue(len(group) in caseTrue)
        for group in groups:
            self.assertFalse(len(group) not in caseTrue)

        max_persons = 5
        num_of_groups = calculate_groups(self.list25persons, max_persons)
        groups = make_groups(num_of_groups, self.list25persons, max_persons)
        for group in groups:
            self.assertTrue(len(group) == 5)
        for group in groups:
            self.assertFalse(len(group) == 5)
