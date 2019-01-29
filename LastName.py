authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

def separate_name(lst):
  new_lst = lst.split(",")
  print(type(lst))
  print(type(new_lst))
  return new_lst

author_names = separate_name(authors)
print(author_names)

#def find_last_names(lst):
#  new_lst = [name.split()[-1] for name in author_names]
#  print(type(lst))
#  print(type(new_lst))
#  return new_lst


def find_last_names(lst):
  new_lst = []
  for name in lst:
    new_lst.append(name.split()[-1])
  return new_lst  


author_last_names = find_last_names(author_names)
print(author_last_names)
