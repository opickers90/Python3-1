class Chess:
  def __init__(self):
    pass

  def play(self):
    print("Playing chess!")

class Checkers:
  def __init__(self):
    pass

  def play(self):
    print("Playing checkers!")    

def play_game(chess_or_checkers):
  chess_or_checkers.play()

chess_game = Chess()
checkers_game = Checkers()
chess_game_2 = Chess()

for game in [chess_game, checkers_game, chess_game_2]:
  play_game(game)
