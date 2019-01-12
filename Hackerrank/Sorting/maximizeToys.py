#Maximize Toys
#Given a list of prices and a maximum amount to spend, 
#determines the maxumum number of toys that can be purchased.

#Since we want to maximize the number of toys, the toys in the solution
#will always be the cheapest toys in the list. Therefore, this program 
#simply sorts them and iterates through them, starting at the cheapest,
#adding each to the purchased items count until the budget has been reached.
import unittest

def maximumToys(prices, budget):
    prices.sort()
    totalCost = 0
    toys = 0
    for i in prices:
        if totalCost+i <= budget:
            totalCost += i
            toys +=1
        else:
        	return toys

class Test(unittest.TestCase):
	def test1(self):
		arr = [1, 12, 5, 111, 200, 1000, 10]
		self.assertEqual(maximumToys(arr, 50), 4)

	def test_all_but_one_larger(self):
		arr = [50, 60, 90, 10]
		self.assertEqual(maximumToys(arr, 40), 1)

	def test_all_larger(self):
		arr = [50, 60, 70]
		self.assertEqual(maximumToys(arr, 10), 0)

	def test_all_smaller(self):
		arr = [1, 2, 3, 4, 5, 6]
		self.assertEqual(maximumToys(arr, 10), 4)

if __name__ == "__main__":
    unittest.main()