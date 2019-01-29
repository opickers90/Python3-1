winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

def join_string(lst):
  lst = "\n".join(lst)
  return lst

winter_trees_full = join_string(winter_trees_lines)
print(winter_trees_full)
