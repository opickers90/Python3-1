inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

inventory_len = len(inventory)
print(inventory_len)
first = inventory[0]
print (first)
last = inventory[-1]
print (last)
inventory_2_6 = inventory [2:6]
print(inventory_2_6)
first_3 = inventory[:3]
print (first_3)
twin_beds = inventory.count("twin bed")
print(twin_beds)
inventory.sort()
print(inventory)

def remove_duplicates(x):
  x.sort()
  new_list= []
  for n in x:
    if n not in new_list:
      new_list.append(n)
  return new_list

no_duplicted = remove_duplicates(inventory)
print (no_duplicted)
print (len(no_duplicted))
