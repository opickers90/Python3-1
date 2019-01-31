# Write your reverse_string function here:
def reverse_string(word):
  new_word = ""
  for char in range(len(word), 0, -1):
    new_word += word[char-1]
  return new_word

# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print
