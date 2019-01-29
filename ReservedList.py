def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    print ("This is lst1 index : {}".format(index))
    print ("This is lst2 index - : {}".format(len(lst2) - 1 - index ))
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True
    
#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
