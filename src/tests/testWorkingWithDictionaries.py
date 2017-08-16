import unittest
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__)+'/..', '..'))
from src import workingWithDictionaries

class TestWorkingWithDictionaries(unittest.TestCase):

    def test_get_age_from_name(self):
        wwd = workingWithDictionaries.WorkingWithDictionaries()
        self.assertEqual(wwd.getAgeFromName('Jon'), 18)
        self.assertEqual(wwd.getAgeFromName('Sam'), 56)

if __name__ == '__main__':
    unittest.main()
