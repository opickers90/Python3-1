#python 3.7.1

class Parking:
  def __init__(self, lst):
      self.lst = lst
      self.slot = []
      
  def display_slot(self):
      for num in self.lst:
          self.slot.append(0)
      print (self.slot)
      
  def adding_car(self,index):
      for num in self.slot:
          try:
              if self.slot[index] == 0:
                 self.slot[index] = 1
                 break
              else:
                 print ("This slot is occupied")
                 break
          except IndexError:
                 print ("That parking slot not available")
                 break
      print (self.slot)
      
      
  def remove_car(self,index):
      try:
          self.slot[index] = 0
          print (self.slot)    
      except IndexError:
          print ("That parking slot not available")
                 
      
def main():
    print ("\"Welcome to Simple Parking system\"\n")
    slot = range(int(input("How many space parking you have :\n")))
    parking = Parking(slot)
    print ("This is your parking space")
    parking.display_slot()
    
main()

"""
Parking.adding_car(0)
Parking.adding_car(1)
Parking.adding_car(2)
Parking.adding_car(3)
Parking.adding_car(4)
Parking.adding_car(1)
Parking.adding_car(6)
Parking.adding_car(10)
Parking.remove_car(1)
Parking.remove_car(1)
Parking.remove_car(10)
"""
