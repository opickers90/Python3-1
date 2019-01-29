print("-------------------------------------------------------")
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)
print("-------------------------------------------------------")
print("-------------------------------------------------------")
def split_csv(csv):
  new_csv = csv.split(",")
  return new_csv

highlighted_poems_list = split_csv(highlighted_poems)
print(highlighted_poems_list)
print(type(highlighted_poems_list))
print("-------------------------------------------------------")
print("-------------------------------------------------------")
def strip_whitespace(lst):
  new_lst = []
  for line in lst:
    new_lst.append(line.strip())
  return new_lst

highlighted_poems_stripped = strip_whitespace(highlighted_poems_list)
print(highlighted_poems_stripped)
print("-------------------------------------------------------")
highlighted_poems_details = []
print("-------------------------------------------------------")
def split_double_colon(lst):
  new_lst = []
  for line in lst:
    new_lst.append(line.split(":"))
  return new_lst

highlighted_poems_details += split_double_colon(highlighted_poems_stripped)
print(highlighted_poems_details)
print("-------------------------------------------------------")
print("-------------------------------------------------------")

def split_titles_poets_dates(lst):
  titles = []
  poets = []
  dates = []
  for word in lst:
    titles.append(word[0])
    poets.append(word[1])
    dates.append(word[2])
  return titles, poets, dates
  
poem = split_titles_poets_dates(highlighted_poems_details)
print(poem)

print("-------------------------------------------------------")
print("-------------------------------------------------------")

def word_combine(lst):
  titles = lst[0]
  poets = lst[1]
  dates = lst[2]
  for n in range(0, len(titles),1):
    print ("{number}. The poem {title} was published by {poet} in {date}.".format(title = titles[n], poet = poets[n], date = dates[n], number = n+1))

word_combine(poem)




