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
    return True, None

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
