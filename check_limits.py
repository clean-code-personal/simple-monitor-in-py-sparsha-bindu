class BatteryParameter:
    def __init__(self, name, value, lower_limit, upper_limit):
        self.name = name
        self.value = value
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    def is_out_of_range(self):
        return self.value < self.lower_limit or self.value > self.upper_limit

    def get_breach_type(self):
        if self.is_out_of_range():
            if self.value < self.lower_limit:
                return "low"
            else:
                return "high"
        return None

class Battery:
    def __init__(self, temperature, soc, charge_rate):
        self.temperature = BatteryParameter("Temperature", temperature, 0, 45)
        self.soc = BatteryParameter("State of Charge", soc, 20, 80)
        self.charge_rate = BatteryParameter("Charge Rate", charge_rate, 0, 0.8)

    def is_ok(self):
        failed_params = self.get_failed_params()
        return not failed_params, failed_params

    def get_failed_params(self):
        battery_parameters = [self.temperature, self.soc, self.charge_rate]
        return [param for param in battery_parameters if param.is_out_of_range()]

    def get_vitals_with_breach(self):
        vitals = []
        battery_parameters = [self.temperature, self.soc, self.charge_rate]
        for param in battery_parameters:
            breach_type = param.get_breach_type()
            if breach_type:
                vitals.append((param.name, breach_type, param.value))
        return vitals

def check_battery(battery):
    result = battery.is_ok()
    if result[0]:
        print("Battery is OK.")
    else:
        print("Battery is not OK.")
        for vital in battery.get_vitals_with_breach():
            print(f"{vital[0]} is {vital[1]} ({vital[2]}).")


