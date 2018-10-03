import unittest
from command import *

class TestCommand(unittest.TestCase):
    def test_command(self):
        remote = Remote()
        tv = Tv()
        tvOn = TvOnCommand(tv)
        tvOff = TvOffCommand(tv)
        remote.set_command(tvOn)
        remote.press_power_button()
        self.assertTrue(tv.get_on())
        remote.set_command(tvOff)
        remote.press_power_button()
        self.assertFalse(tv.get_on())

if __name__ == '__main__':
    unittest.main()
