battery_limit = {
     'temperature': {'min': 0, 'max': 45},
     'soc': {'min': 20, 'max': 80},
     'roc': {'min': 0,'max': 0.8}
        } 
         
def check_attribute_stable(bms_attribute):
    offLimits = []
    for bms_name,bms_value in bms_attribute.items() :
        check_attribute_limit(bms_name,bms_value,offLimits)       
    return offLimits

def check_attribute_limit(bms_name,bms_value,offLimits):
     if (bms_value < bms_attribute_limits[bms_name]['min']) or (bms_value > bms_attribute_limits[bms_name]['max']):
            offLimits.append(bms_name)

def battery_is_ok(battery_Values):
     bms_vitals = check_attribute_stable(bms_attribute)
    
     if len(bms_vitals) == 0:
          print("battery working condition are good")
      else:
          print("Battery maybe having some troubles! Please check")


if __name__ == '__main__':
  assert(battery_is_ok({'temperature': 25,'soc': 70, 'roc': 0.7}) is True)
  assert(battery_is_ok({'temperature': 50,'soc': 85, 'roc': 0}) is False)
