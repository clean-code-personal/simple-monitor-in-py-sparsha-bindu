def check_temperature(temperature):
  if temperature < 0:
    return False, 'low'
  elif temperature > 45:
    return False, 'high'
  else:
    return True, None

def check_soc(soc):
  if soc < 20:
    return False, 'low'
  elif soc > 80:
    return False, 'high'
  else:
    return True, None

def check_charge_rate_ok(charge_rate):
  if charge_rate > 0.8:
    return False, 'high'
  else:
    return True, 'low'

def print_error_message(vital_name, breach_type):
  print('{} is {}!'.format(vital_name, breach_type))
  
def is_battery_ok(temperature, soc, charge_rate):
  ok = True
  vital_name = None
  breach_type = None

  # check temperature
  is_ok, breach_type = check_temperature(temperature)
  if not is_ok:
    ok = False
    vital_name = 'temperature'

  # check state of charge
  is_ok, breach_type = check_soc(soc)
  if not is_ok:
    ok = False
    vital_name = 'state of charge'

  # check charge rate
  is_ok, breach_type = check_charge_rate_ok(charge_rate)
  if not is_ok:
    ok = False
    vital_name = 'charge rate'

  if not ok:
    return False, vital_name, breach_type
  else:
    return True, None, None

def battery_status(temperature, soc, charge_rate, reporter=print_error_message):
  is_ok, vital_name, breach_type = is_battery_ok(temperature, soc, charge_rate)
  if not is_ok:
    reporter(vital_name, breach_type)
  return is_ok,vital_name,breach_type

if __name__ == '__main__':
    assert(battery_status(25, 70, 0.7) == (True, None, None))
    assert(battery_status(-5, 70, 0.7) == (False, 'temperature', 'low'))
    assert(battery_status(50, 70, 0.7) == (False, 'temperature', 'low'))
    assert(battery_status(25, 10, 0.7) == (False, 'state of charge', 'low'))
    assert(battery_status(25, 90, 0.7) == (False, 'state of charge', 'low'))
    assert(battery_status(25, 70, 0.9) == (False, 'charge rate', 'high'))
