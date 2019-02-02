from datetime import time

print("--------------------------------------------------")
print("Making the Menus")
print("__________________________________________________")

class Menu:
  
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
    
  def __repr__(self):
    return "{menu_name} Menu available from {start_time}:00 to {end_time}:00.".format(menu_name = self.name, start_time = self.start_time, end_time = self.end_time)
  
  def calculate_bill(self, purchased_items):
    total_bill = 0
    for item in purchased_items:
      total_bill += self.items[item]
    return "Your Bill is: {bill}".format(bill = total_bill)  
  
brunch_menu = {
  'pancakes': 7.50, 
  'waffles': 9.00, 
  'burger': 11.00, 
  'home fries': 4.50, 
  'coffee': 1.50, 
  'espresso': 3.00, 
  'tea': 1.00, 
  'mimosa': 10.50, 
  'orange juice': 3.50
}

early_bird_menu = {
  'salumeria plate': 8.00, 
  'salad and breadsticks (serves 2, no refills)': 14.00, 
  'pizza with quattro formaggi': 9.00, 
  'duck ragu': 17.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 1.50, 
  'espresso': 3.00,
}

dinner_menu = {
  'crostini with eggplant caponata': 13.00, 
  'ceaser salad': 16.00, 
  'pizza with quattro formaggi': 11.00, 
  'duck ragu': 19.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 2.00, 
  'espresso': 3.00,
}

kids_menu = {
  'chicken nuggets': 6.50, 
  'fusilli with wild mushrooms': 12.00, 
  'apple juice': 3.00
}

brunch = Menu("Brunch", brunch_menu, 11, 16)    
early_bird = Menu("Early Bird", early_bird_menu, 15, 18)    
dinner = Menu("Dinner", dinner_menu, 17, 23)    
kids = Menu("Kids", kids_menu, 11, 21)    

print(brunch)
print(early_bird)
print(dinner)
print(kids)



print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

#Other Example
#print(brunch.calculate_bill(['pancakes', 'home fries']))
#print(dinner.calculate_bill(['ceaser salad', 'pizza with quattro formaggi', 'coffee', 'coffee', 'espresso']))
#print(kids.calculate_bill(['chicken nuggets', 'apple juice']))

#Note create Exception for this KeyError
#print(brunch.calculate_bill(['chicken nuggets', 'apple juice']))



print("--------------------------------------------------")
print("Creating the Franchises")
print("__________________________________________________")

class Franchise:
  
  def __init__(self, address, menus = [brunch, early_bird, dinner, kids]):
    self.address = address 
    self.menus = menus
    
  
  def __repr__(self):
    return "Our Franchise is located in {address} and have {menus}".format(address = self.address, menus = self.menus)
  
  def available_menus(self,time):
    #available_menu = []
    print ("Menu that available at {time}:00 :".format(time = time))
    print ("-------------------------------------")
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        print (menu)
    print ("-------------------------------------")
  

flagship_store = Franchise("1232 West End Road")
new_installment = Franchise("1232 West End Road")

flagship_store.available_menus(12)
flagship_store.available_menus(17)



print("--------------------------------------------------")
print("Creating Businesses")
print("__________________________________________________")

class Business:
  
  def __init__ (self, name, franchises = [flagship_store, new_installment]):
    self.name = name
    self.franchises = franchises
    
  def __repr__(self):
    return "{name} and {franchises}".format(name = self.name, franchises = self.franchises)

basta = Business("Basta Fazoolin' with my Heart")    
#print(basta)
  
  
arepas_menu = {
  'arepa pabellon': 7.00, 
  'pernil arepa': 8.50, 
  'guayanes arepa': 8.00, 
  'jamon arepa': 7.50
}
  
arepas = Menu("Take a' Arepa", arepas_menu, 10, 22)
print (arepas)
arepas_place = Franchise("189 Fitzgerald Avenue", arepas)
print (arepas_place)
arepas_business = Business("Take a' Arepa", arepas_place)  
print(arepas_business) 














