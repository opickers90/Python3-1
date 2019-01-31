# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  new_dict = {}
  for word in words:
    new_dict[word] = 1 
    if word in new_dict:
      new_dict[word] += 1
  return new_dict  
    
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

