#Minimum Swaps
#Given an unordered array consisting of consecutive integers [1, 2, 3, ..., n] without any duplicates,
#finds the minimum number of swaps required to sort the array in ascending order.

import unittest

def minimumSwaps(arr):
	swaps = 0
	i = 0
	while i<len(arr):
		if arr[i]==(i+1):
			i+=1
			continue
		arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
		swaps+=1
	return swaps

class Test(unittest.TestCase):
	def test_sorted_list(self):
		input = [1, 2, 3]
		output = minimumSwaps(input)
		self.assertEqual(output, 0)

	def test_single_swap(self):
		input = [1, 3, 2]
		output = minimumSwaps(input)
		self.assertEqual(output, 1)

	def test_reverse_sorted(self):
		input = [3, 2, 1]
		output = minimumSwaps(input)
		self.assertEqual(output, 1)

if __name__ == "__main__":
	unittest.main()