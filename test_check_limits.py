
import unittest
from check_limits import Battery,check_battery

class TestBatteryIsOk(unittest.TestCase):
    def test_battery_is_ok(self):
        self.assertTrue(check_battery(Battery(25, 70, 0.7, "Celcius",'en')))
        self.assertFalse(check_battery(Battery(-5, 60, 0.6, "Celcius",'ge')))
        self.assertFalse(check_battery(Battery(104, 90, 0.7, "Fahrenheit",'kn')))
        self.assertFalse(check_battery(Battery(86, 75, 0.9, "Fahrenheit",'fr')))


if __name__ == '__main__':
    unittest.main()
