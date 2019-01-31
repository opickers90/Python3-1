letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
print(letters)
print(points)
print("------------------------------------------")
letters += [letter.lower() for letter in letters]
points *= 2
print(letters)
print(points)
print("------------------------------------------")
letter_to_points = {letters:points for letters, points in zip(letters, points)}
print(letter_to_points)
print("------------------------------------------")
letter_to_points[" "]=0
print(letter_to_points)
print("------------------------------------------")
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter,0)
  return point_total  
  
brownie_points = score_word("BROWNIE")
print("Test Function with inpu \"BROWNIE\"")
print("Score is: ",brownie_points)
print("------------------------------------------")
player_to_words = {
  "player1":["BLUE", "TENNIS", "EXIT"],
  "wordNerd":["EARTH", "EYES", "MACHINE"],
  "lexi Con":["ERASER", "BELLY", "HUSKY"],
  "Prof Reader":["ZAP", "COMA", "PERioD"]
}
player_to_points = {}
print(player_to_words)
print(player_to_points)
print("------------------------------------------")
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    print("Player's name : {name}".format(name = player))
    for word in words:
      player_points += score_word(word)
      print("Score for this word [{word}] is {score}.".format(word = word, score = score_word(word)))
    print("Score total is: ", player_points)
    print("--------------------------------")
    player_to_points[player]=player_points  
  return player_to_points


update_point_totals()
print("------------------------------------------")
print("Extention")
print("------------------------------------------")
def play_word(player, word):
  player_to_words[player].append(word)

play_word("player1", "HELLO")
play_word("player1", "morning")
update_point_totals()



