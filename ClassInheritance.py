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
  
print(vehicle.get_rate())
print(home.get_rate())
