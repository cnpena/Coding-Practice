#Comparator
#Given an array of Player objects, uses a comparator to sort them
#in order of decreasing score. If two players have the same score, 
#they are sorted alphabetically.

from functools import cmp_to_key

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def comparator(a, b):
        if a.score < b.score:
            return 1
        elif a.score > b.score:
            return -1
        elif a.name > b.name:
            return 1
        else:
            return -1


class Test(unittest.TestCase):
    def test_no_duplicate_values(self):
        #

    def test_only_duplicate_values(self):
        #

if __name__ == "__main__":
    unittest.main()

# data = [['amy', 100], ['david', 100], ['heraldo', 50], ['aakansha', 75], ['aleksa', 150]]
# players = []
# for i in data:
#     name, score = i[0], i[1]
#     player = Player(name, score)
#     players.append(player)
    
# players = sorted(players, key=cmp_to_key(Player.comparator))
# for i in players:
#     print(i.name, i.score)