import language

class Battery:
    def __init__(self, temperature, soc, charge_rate, temp_unit, lang):
        self.temperature = temperature
        self.soc = soc
        self.charge_rate = charge_rate
        self.temp_unit = temp_unit
        self.lang = lang

    def battery_is_ok(self):
        
        self.temperature = convert_to_celsius(self.temperature, self.temp_unit)
        return (is_ok(self.temperature, 0, 45, language.messages[self.lang]['temperature'], self.lang, self.temp_unit) and
                is_ok(self.soc, 20, 80, language.messages[self.lang]['soc'], self.lang) and
                is_ok(self.charge_rate, 0, 0.8, language.messages[self.lang]['chargeRate'], self.lang))

def is_ok(input_val, lower_limit, upper_limit, breach_type, lang, unit=""):
    if input_val < lower_limit or input_val > upper_limit:
        print(language.messages[lang]['outOfRange'](breach_type))
        return False
    return True

def convert_to_celsius(temperature, unit):
    if unit =='Fahrenheit': 
        return (temperature - 32) * 5/9
    return temperature


def check_battery(battery):
    if battery.battery_is_ok():
        print(language.messages[battery.lang]['batteryOk'])
        return True
    else:
        print(language.messages[battery.lang]['batteryNotOk'])
        return False
