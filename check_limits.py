def check_vital(vital_name, value, min_value, max_value):
  if value < min_value:
    return False, 'low'
  elif value > max_value:
    return False, 'high'
  else:
    return True, None

def is_battery_ok(temperature, soc, charge_rate):
  is_temp_ok, temp_breach_type = check_vital('temperature', temperature, 0, 45)
  is_soc_ok, soc_breach_type = check_vital('state of charge', soc, 20, 80)
  is_charge_rate_ok, charge_breach_type = check_vital('charge rate', charge_rate, 0, 0.8)
  
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

if __name__ == '__main__':
  assert(battery_status(25, 70, 0.7) is True)
  assert(battery_status(50, 85, 0) is False)
  assert(battery_status(-5, 40, 0) is False)
  assert(battery_status(50, 85, 0)[1] == 'state of charge')
  assert(battery_status(50, 85, 0)[2] == 'high')
