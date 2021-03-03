battery_limit = {
     'temperature': {'min': 0, 'max': 45},
     'soc': {'min': 20, 'max': 80},
     'roc': {'min': 0,'max': 0.8}
        } 
def battery_range_parameters(battery_Values,parameter_off_Limit):
  for parameter_name,parameter_value in battery_Values.items() :
     if (parameter_value < battery_limit[parameter_name]['min']) or (parameter_value >battery_limit[parameter_name]['max']):
          parameter_off_Limits.append(parameter_name)
          return parameter_off_Limits

def battery_is_ok(battery_Values):
  parameter_off_Limit=[]
  result=battery_range_parameters(battery_Values,parameter_off_Limit)
  if len(result)==0 :
    print('battery working condition are good')
    return true
  else: 
    print('Battery maybe having some troubles! Please check')
    return False


if __name__ == '__main__':
  assert(battery_is_ok({'temperature': 25,'soc': 70, 'roc': 0.7}) is True)
  assert(battery_is_ok({'temperature': 50,'soc': 85, 'roc': 0}) is False)
