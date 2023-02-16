import unittest
from check_limits import Battery, check_battery

class TestBattery(unittest.TestCase):
    def test_battery_ok(self):
        battery = Battery(25, 70, 0.7)
        self.assertFalse(check_battery(battery))

    def test_battery_temperature_low(self):
        battery = Battery(-5, 70, 0.7)
        self.assertFalse(check_battery(battery))
    
    def test_battery_temperature_high_soc_high(self):
        battery = Battery(50, 85, 0)
        self.assertFalse(check_battery(battery))

    def test_battery_soc_low_charge_rate_high(self):
        battery = Battery(0, 20, 0.8)
        self.assertFalse(check_battery(battery))

    def test_battery_soc_high_charge_rate_high(self):
        battery = Battery(45, 80, 0.8)
        self.assertFalse(check_battery(battery))

    def test_battery_temperature_low_soc_low_charge_rate_low(self):
        battery = Battery(-1, 19, -1)
        self.assertFalse(check_battery(battery))

    def test_battery_temperature_high_soc_high_charge_rate_high(self):
        battery = Battery(46, 81, 0.9)
        self.assertFalse(check_battery(battery))

    def test_battery_temperature_ok_soc_ok_charge_rate_ok(self):
        battery = Battery(22, 60, 0.4)
        self.assertFalse(check_battery(battery))

if __name__ == '__main__':
    unittest.main()
