battery_limit = {
     'temperature': {'min': 0, 'max': 45},
     'soc': {'min': 20, 'max': 80},
     'roc': {'min': 0,'max': 0.8}
        } 
         
def battery_parameters_Check(battery_Values):
    parameter_off_Limits = []
    for parameter_name,parameter_value in battery_Values.items() :
        check_attribute_limit(parameter_name,parameter_value,parameter_off_Limits)       
    return parameter_off_Limits

def check_attribute_limit(parameter_name,parameter_value,parameter_off_Limits):
     if (parameter_value < battery_limit[parameter_name]['min']) or (parameter_value > battery_limit[parameter_name]['max']):
            parameter_off_Limits.append(parameter_name)

def battery_is_ok(battery_Values):
     battery_parameters = battery_parameters_Check(battery_Values)
    if len(battery_parameters) == 0 :
          print("Battery working conditons are good")
     else:
          print("please check")


if __name__ == '__main__':
  assert(battery_is_ok({'temperature': 25,'soc': 70, 'roc': 0.7}) is True)
  assert(battery_is_ok({'temperature': 50,'soc': 85, 'roc': 0}) is False)
