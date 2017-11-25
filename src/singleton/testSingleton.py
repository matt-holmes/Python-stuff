import unittest
from single import Single

class TestSingleton(unittest.TestCase):
   # instance = Single()

    def test_only_one_instance(self):
        x = Single('golf')
        self.assertEqual(x.getValue(), 'golf')
        y = Single('bowling')
        self.assertEqual(y.getValue(), 'bowling')
        z = Single('darts')
        self.assertEqual(z.getValue(), 'darts')
        self.assertEqual(y.getValue(), 'darts')
        self.assertEqual(x.getValue(), 'darts')

if __name__ == '__main__':
    unittest.main()
