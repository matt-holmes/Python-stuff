import unittest
from strategy import *

class TestStrategy(unittest.TestCase):
    def test_strategy(self):
        sans = SansFontStrategy()
        mono = MonoFontStrategy()
        fontContext = FontContext(sans)
        self.assertEqual(fontContext.context_interface(), 'using sans font')
        fontContext = FontContext(mono)
        self.assertEqual(fontContext.context_interface(), 'using mono font')

if __name__ == '__main__':
    unittest.main()
