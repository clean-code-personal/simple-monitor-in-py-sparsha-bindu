import unittest
from check_limits import battery_status

class TestBMS(unittest.TestCase):
    def test_bms(self):
        self.assertFalse(battery_status(25, 70, 0.7))
        self.assertFalse(battery_status(50, 85, 0))
        self.assertFalse(battery_status(-5, 40, 0)[0])
        self.assertIs(battery_status(50, 85, 0)[1],'state of charge')
        self.assertIs(battery_status(50, 85, 0)[2], 'high')

if __name__ == '__main__':
    unittest.main()
