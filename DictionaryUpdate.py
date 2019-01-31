drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

print(drinks)
print(caffeine)

zipped_drinks = zip(drinks, caffeine)
#print(list(zipped_drinks))
#print(tuple(zipped_drinks))

# First method using list comprehensions
drinks_to_caffeine = {key:value for key, value in zipped_drinks}


#drinks_to_caffeine = {}
#for key, value in zipped_drinks:
  # second method, itteration and using add key value
  #drinks_to_caffeine[key] = value
  # third method, itteration and using update key value
  #drinks_to_caffeine.update({key:value})


print (drinks_to_caffeine)

