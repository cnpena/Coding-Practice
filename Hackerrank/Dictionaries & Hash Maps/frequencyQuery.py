#Frequency Queries
#Given an array of queries of the form two integers:
#   [1, x]: Insert x in data structure
#   [2, y]: Delete one occurence of y from data structure, if present
#   [3, z]: If any integer is present whose frequency is exactly z, print 1 else 0.
# Output: Returns an integer array consisting of all the outputs of queries of type 3.

from collections import defaultdict
import unittest

#Works by using two tables. The first serves as a lookup table, containing each value
#and it's frequency. The other serves as a frequency table where each key is a frequency
#and value is the set of values with that frequency.

def freqQuery(queries):
    output = []
    lookup = dict()
    freqs = defaultdict(set)

    for command, value in queries:
        freq = lookup.get(value, 0)
        if command == 1:
            lookup[value] = freq + 1
            freqs[freq].discard(value)
            freqs[freq + 1].add(value)
        elif command == 2:
            lookup[value] = max(0, freq - 1)
            freqs[freq].discard(value)
            freqs[freq - 1].add(value)
        elif command == 3:
            output.append(1 if freqs[value] else 0)
            
    return output

class Test(unittest.TestCase):
    def test_1(self):
        queries = [[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]
        self.assertEqual(freqQuery(queries), [0,1])

    def test_2(self):
        queries = [[3, 4], [2, 1003], [1, 16], [3, 1]]
        self.assertEqual(freqQuery(queries), [0, 1])

    def test_3(self):
        queries = [[1, 3], [2, 3], [3, 2], [1, 4], [1, 5], [1, 5], [1, 4], [3, 2], [2, 4], [3, 2]]
        self.assertEqual(freqQuery(queries), [0, 1, 1])
        
if __name__ == "__main__":
    unittest.main()