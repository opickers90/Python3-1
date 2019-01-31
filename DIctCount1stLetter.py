# Write your count_first_letter function here:
#def count_first_letter(names):
#  new_dict = {}
#  for key in names:
#    if key[0] not in new_dict:
#      new_dict[key[0]] = 0
#    new_dict[key[0]] += len(names[key])
#  return new_dict

def count_first_letter(names):
  new_dic = {}
  for key in names.keys():
    if key[0] not in new_dic:
      new_dic[key[0]] = len(names[key])
    else:
      new_dic[key[0]] += len(names[key])
  return new_dic  

# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
