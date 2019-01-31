# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  return {word:words.count(word) for word in words}
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}
