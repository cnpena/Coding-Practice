#Comparator
#Given an array of Player objects, uses a comparator to sort them
#in order of decreasing score. If two players have the same score, 
#they are sorted alphabetically.

from functools import cmp_to_key
import unittest

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

#To facilitate testing
def asString(arr):
    players = []
    for i in arr:
        players.append([i.name, i.score])
    return players

class Test(unittest.TestCase):
    def test_no_duplicate_values(self):
        players = [Player('A', 1), Player('B', 2), Player('C', 3)]
        playersSorted = sorted(players, key=cmp_to_key(Player.comparator))
        self.assertEqual(asString(playersSorted), [['C', 3], ['B', 2], ['A', 1]])

    def test_all_duplicate_values(self):
        players = [Player('C', 1), Player('B', 1), Player('A', 1)]
        playersSorted = sorted(players, key=cmp_to_key(Player.comparator))
        self.assertEqual(asString(playersSorted), [['A', 1], ['B', 1], ['C', 1]])

    def test_duplicate_names(self):
        players = [Player('A', 1), Player('B', 3), Player('A', 2)]
        playersSorted = sorted(players, key=cmp_to_key(Player.comparator))
        self.assertEqual(asString(playersSorted), [['B', 3], ['A', 2], ['A', 1]])

if __name__ == "__main__":
    unittest.main()
