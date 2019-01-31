# Write your every_other_letter function here:
def every_other_letter(word):
  if len(word) > 0:
    for char in range(len(word)):
      return word[::2]
  return ""  
        

# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 
