#Write your function here
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    print ("This is before: {}".format(lst))
    lst = lst[1:]
    print ("This is after: {}".format(lst))
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
print(delete_starting_evens([]))


