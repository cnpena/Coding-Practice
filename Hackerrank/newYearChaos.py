#New Year Chaos
#There are a number of people queued up, and each person wears a sticker indicating
#their initial position in the queue. Initial positions increment by 1 from 1 at
#the front of the line to n at the back. Any person in the queue can bribe the
#person directly in front of them to swap positions. If two people swap positions,
#they still wear the same sticker denoting their original places in line. One
#person can bribe at most two others.

#This program finds the minimum number of bribes that took place to get the queue
#into its current state

import unittest

#Iterates through the array, first checking if it is possible to get this configuration
#with every person only bribing at most two others. In order for this to be true, 
#no person should be more than two places in front of where they started.
#Otherwise if valid, counts the swaps that took place.
def minimumBribes(q):
	bribes = 0
	for index, value in enumerate(q):
		if (value - 1) - index > 2:
			return 'Too chaotic'

		for j in range(max(0, q[index] - 2), index):
			if q[j] > q[index]:
				bribes+=1
	return bribes

class Test(unittest.TestCase):
	validLines = [[2, 1, 5, 3, 4], [1, 2, 5, 3, 7, 8, 6, 4]]
	validLinesSol = [3, 7]

	chaoticLines = [[2, 5, 1, 3, 4], [5, 1, 2, 3, 7, 8, 6, 4]]

	def test_valid_lines(self):
		for i in range(len(self.validLines)):
			self.assertEquals(minimumBribes(self.validLines[i]), self.validLinesSol[i])

	def test_chaotic_lines(self):
		for i in range(len(self.chaoticLines)):
			self.assertEquals(minimumBribes(self.chaoticLines[i]), 'Too chaotic')

if __name__ == "__main__":
	unittest.main()