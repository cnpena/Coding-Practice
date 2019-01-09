#Ransom Note
#Given an array of words in a magazine and an array of words in a 
#desired ransom note, determines whether it is possible to make the 
#note with the given magazine.
#Words are case sensitive.
import unittest

def checkMagazine(magazine, note):
    #First, put all words from magazine into hash table and the # of 
    #times they appear 
    magazineTable = {}
    for i in magazine:
        if i not in magazineTable:
            magazineTable[i] = 1
        else:
            magazineTable[i] += 1
    
    #Iterate through the words in the note. If a word does not exist in
    #the magazine table, immediately return false. Otherwise, remove it from
    #the table.
    for i in note:
        if i in magazineTable:
            if magazineTable[i] > 1:
                magazineTable[i] -=1
            else:
                magazineTable.pop(i)
        else:
            return False
    return True

class Test(unittest.TestCase):

    def test_duplicate_words_false(self):
        magazine = ['two', 'times', 'three', 'is', 'not', 'four']
        note = ['two', 'times', 'two', 'is', 'four']

        self.assertFalse(checkMagazine(magazine, note))

    def test_duplicate_words_True(self):
        magazine = ['two', 'times', 'two', 'is', 'not', 'four']
        note = ['two', 'times', 'two', 'is', 'four']

        self.assertTrue(checkMagazine(magazine, note))

    def test_exact_same_words(self):
        magazine = ['two', 'times', 'three', 'is', 'not', 'four']
        note = ['two', 'times', 'three', 'is', 'not', 'four']

        self.assertTrue(checkMagazine(magazine, note))

    def test_subset_words(self):
        magazine = ['two', 'times', 'three', 'is', 'not', 'four']
        note = ['two', 'times', 'is', 'four']

        self.assertTrue(checkMagazine(magazine, note))

if __name__ == "__main__":
    unittest.main()