import unittest
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__)+'/..', '..'))
from src import datastructures

class TestDatastructures(unittest.TestCase):

    def test_get_age_from_name_from_dictionary(self):
        inst = datastructures.Datastructures()
        self.assertEqual(inst.get_age_from_dict('Jon'), 18)
        self.assertEqual(inst.get_age_from_dict('Sam'), 56)

    def test_dictionary_key_doesnt_exist(self):
        inst = datastructures.Datastructures()
        self.assertEqual(inst.get_age_from_dict('Alex'), None)

if __name__ == '__main__':
    unittest.main()
