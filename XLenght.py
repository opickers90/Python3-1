# Write your x_length_words function here:
def x_length_words(sentence, x):
  split_sent = sentence.split(" ")
  for word in split_sent:
    if (len(word)) < x:
    	return False
  return True  
  
# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
