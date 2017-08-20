import unittest
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__)+'/..', '..'))
from src import datastructures

class TestDatastructures(unittest.TestCase):

    inst = datastructures.Datastructures()

    def test_get_age_from_name_from_dictionary(self):
        self.assertEqual(self.inst.get_age_from_name_from_dict('Jon'), 18)
        self.assertEqual(self.inst.get_age_from_name_from_dict('Sam'), 56)

    def test_dictionary_key_doesnt_exist(self):
        self.assertEqual(self.inst.get_age_from_name_from_dict('Alex'), None)

    def test_list_append(self):
        self.inst.get_list().append('billy')
        self.assertEqual(len(self.inst.get_list()), 5)

    def test_list_pop(self):
        self.inst.get_list().pop()
        self.assertEqual(len(self.inst.get_list()), 4)
        self.assertEqual(self.inst.get_list()[2], 'sam')

    def test_create_new_list_upper(self):
        a_list = self.inst.create_new_list_upper()
        self.assertEqual(a_list[0], 'JON')
        self.assertEqual(a_list[1], 'ALEX')
        self.assertEqual(a_list[2], 'SAM')
        self.assertEqual(a_list[3], 'JANE')

    def test_create_new_dict_upper_last_name(self):
        a_dict = self.inst.create_new_dict_upper_last_name()
        self.assertEqual(a_dict['Jon'][1], 'SMITH')
        self.assertEqual(a_dict['Sam'][1], 'GREEN')


if __name__ == '__main__':
    unittest.main()
