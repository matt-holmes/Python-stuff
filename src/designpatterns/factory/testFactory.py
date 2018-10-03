import unittest
from factory import *

class TestFactory(unittest.TestCase):
    def test_factory(self):
        factory = Factory()
        result = factory.getFootwear("lazy")
        self.assertEqual(result.action(), "walking")

        result = factory.getFootwear("motivated")
        self.assertEqual(result.action(), "hiking")

        result = factory.getFootwear("energenic")
        self.assertEqual(result.action(), "running")

if __name__ == '__main__':
    unittest.main()
