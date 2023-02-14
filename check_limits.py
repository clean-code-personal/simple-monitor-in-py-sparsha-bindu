class BatteryParameter:
    def __init__(self, name, value, lower_limit, upper_limit):
        self.name = name
        self.value = value
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    def is_out_of_range(self):
        return self.value < self.lower_limit or self.value > self.upper_limit

class Battery:
    def __init__(self, temperature, soc, charge_rate):
        self.temperature = BatteryParameter("Temperature", temperature, 0, 45)
        self.soc = BatteryParameter("State of Charge", soc, 20, 80)
        self.charge_rate = BatteryParameter("Charge Rate", charge_rate, 0, 0.8)

  def is_ok(self):
        battery_parameters = [self.temperature, self.soc, self.charge_rate]
        if any(param.is_out_of_range() for param in battery_parameters):
            failed_params = [param for param in battery_parameters if param.is_out_of_range()]
            return False, failed_params
        else:
            return True

def check_battery(battery):
    result = battery.is_ok()
    if result == True:
        print("Battery is OK.")
    else:
        print("Battery is not OK.")
        for param in result[1]:
            print(f"{param.name} is out of range ({param.lower_limit}-{param.upper_limit}): {param.value}")

if __name__ == '__main__':
    battery = Battery(25, 70, 0.7)
    check_battery(battery)

    battery = Battery(-5,70,0.7)
    check_battery(battery)
    # Output: Battery is OK.

    battery = Battery(50, 85, 0)
    check_battery(battery)
    # Output: Battery is not OK.
    # Temperature is out of range (0-45): 50
    # State of Charge is out of range (20-80): 85
