#Bubble Sort
#Given an array of integers, sorts the array in ascending order
#using Bubble sort. Once sorted, returns the number of swaps required.
#Run time: O(n^2)

import unittest

def countSwaps(a):
    swaps = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if(a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
                swaps +=1
    return swaps

class Test(unittest.TestCase):
	def test_sorted(self):
		arr = [1, 2, 3]
		self.assertEqual(countSwaps(arr), 0)

	def test_reverse_sorted(self):
		arr = [4, 3, 2, 1]
		self.assertEqual(countSwaps(arr), 6)

	def test_unsorted(self):
		arr = [4, 2, 3, 1]
		self.assertEqual(countSwaps(arr), 5)

if __name__ == "__main__":
    unittest.main()
