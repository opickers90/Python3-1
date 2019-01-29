love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']


def strip_whitespaces(lst):
  new_lst = []
  for line in lst:
    new_lst.append(line.strip())
  return new_lst  

def join_string(lst):
  lst = "\n".join(lst)
  return lst

love_maybe_lines_stripped = strip_whitespaces(love_maybe_lines)
print(love_maybe_lines_stripped)
love_maybe_full = join_string(love_maybe_lines_stripped)
print(love_maybe_full)
