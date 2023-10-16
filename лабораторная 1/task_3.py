list_ = ["player1", "player2", "player3", "player4", "player5", "player6"]
num = len(list_)
print("number of players = " + str(num))
a = num//2
print("team 1 = " + str(list_[:a]))
print("team 2 = " + str(list_[a:]))

