class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item
    
class VehicleInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * .001
    

class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * .00005
  
vehicle = VehicleInsurance(2000)
home = HomeInsurance(2000)

def InsuranceTotal(vehicle_or_home):
  print(vehicle_or_home.get_rate())
  
for insurance in [vehicle, home]:
  InsuranceTotal(insurance)

