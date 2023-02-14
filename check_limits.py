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
  is_temp_ok, temp_breach_type = check_temperature(temperature)
  is_soc_ok, soc_breach_type = check_soc(soc)
  is_charge_rate_ok, charge_breach_type = check_charge_rate_ok(charge_rate)
  
  if not is_temp_ok:
    return False, 'temperature', temp_breach_type
  elif not is_soc_ok:
    return False, 'state of charge', soc_breach_type
  elif not is_charge_rate_ok:
    return False, 'charge rate', charge_breach_type
  else:
    return True, None, None

def battery_status(temperature, soc, charge_rate, reporter=print_error_message):
  is_ok, vital_name, breach_type = is_battery_ok(temperature, soc, charge_rate)
  if not is_ok:
    reporter(vital_name, breach_type)
  return is_ok,vital_name,breach_type
