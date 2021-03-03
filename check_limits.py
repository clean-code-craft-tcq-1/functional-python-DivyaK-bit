battery_limit = {
     'temperature': {'min': 0, 'max': 45},
     'soc': {'min': 20, 'max': 80},
     'roc': {'min': 0,'max': 0.8}
        } 
def collect_out_of_range_battery_parameters(parameters_exceeded_limit,parameter_name,parameter_value,parameter_limit):
     if parameter_value < parameter_limit['min'] or parameter_value > parameter_limit['max']:
        parameters_exceeded_limit.append(parameter_name)
         
def report_battery_parameters(Battery_Parameters):
     parameters_exceeded_limit = []
     for battery_parameter in Battery_Parameters:
         collect_out_of_range_battery_parameters(parameters_exceeded_limit,battery_parameter,Battery_Parameters[battery_parameter],limit[battery_parameter])
     return parameters_exceeded_limit

def battery_is_ok(battery_Values):
 result = report_battery_parameters(Battery_Parameters)

  if len(result)==0 :
    print('battery working condition are good')
    return true
  else: 
    print('Battery maybe having some troubles! Please check')
    return False


if __name__ == '__main__':
  assert(battery_is_ok({'temperature': 25,'soc': 70, 'roc': 0.7}) is True)
  assert(battery_is_ok({'temperature': 50,'soc': 85, 'roc': 0}) is False)
