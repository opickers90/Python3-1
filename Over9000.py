#Write your function here
def over_nine_thousand(lst):
  total = 0
  for num in lst:
    total += num
    if total > 9000:
      break
  return total


#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))
