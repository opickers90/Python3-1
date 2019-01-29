def letter_check(word,letter):
  count = 0
  for char in word:
    if char == letter:
      return True
    count +=1
  return False  
    
print(letter_check("strawberry", "o"))
print(letter_check("strawberry", "a"))
