import unittest
from single import Single

class TestSingleton(unittest.TestCase):
   # instance = Single()

    def test_only_one_instance(self):
        x = Single('golf')
        self.assertEqual(x.get_value(), 'golf')
        y = Single('bowling')
        self.assertEqual(y.get_value(), 'bowling')
        z = Single('darts')
        self.assertEqual(z.get_value(), 'darts')
        self.assertEqual(y.get_value(), 'darts')
        self.assertEqual(x.get_value(), 'darts')

if __name__ == '__main__':
    unittest.main()
