# Write your word_length_dictionary function here:
#1st Method
def create_dict1(lst):
  return {word:len(word) for word in lst}

#2nd Method
def create_dict2(lst):
  my_dir = {}
  for word in lst:
    my_dir.update({word:len(word)})
  return my_dir  

#3rd Method  
def create_dict3(lst):
  my_dir = {}
  for word in lst:
    my_dir[word]=len(word)
  return my_dir  

# Uncomment these function calls to test your  function:
print(create_dict1(["apple", "dog", "cat"]))
print(create_dict2(["apple", "dog", "cat"]))
print(create_dict3(["apple", "dog", "cat"]))


