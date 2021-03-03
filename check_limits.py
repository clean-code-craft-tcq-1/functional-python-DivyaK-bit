battery_limit = {
     'temperature': {'min': 0, 'max': 45},
     'soc': {'min': 20, 'max': 80},
     'roc': {'min': 0,'max': 0.8}
        } 
         
def report_battery_parameters(Battery_Parameters):
     parameters_off_limit = []
     for parameters_name,parameters_value in Battery_Parameters.items() :
          
          if (parameters_value < battery_limit[parameters_name]['min']) or (parameters_value > battery_limit[parameters_name]['max']):
               parameters_off_limit.append(parameters_name)
               
     return parameters_off_limit

def battery_is_ok(battery_Values):
     result = report_battery_parameters(Battery_Parameters)
     
     if len(result) == 0:
          print('battery working condition are good')
      else:
          print('Battery maybe having some troubles! Please check')


if __name__ == '__main__':
  assert(battery_is_ok({'temperature': 25,'soc': 70, 'roc': 0.7}) is True)
  assert(battery_is_ok({'temperature': 50,'soc': 85, 'roc': 0}) is False)
