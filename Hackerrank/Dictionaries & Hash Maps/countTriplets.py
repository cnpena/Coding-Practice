#Count Triplets
#Given an array, finds the number of triplets of indices (i, j, k) such that
#the elements at these indices are in geometric progression for a given common ratio.

from collections import Counter
import unittest

#Works by iterating through the array, counting potential and
#actual triplets. For each value in the array, i, add 1 potential
#triplet to r2 (value r*i). If i is a middle triplet value, ie in
#r2, add potential triplet to r3 (value r*i). Finally, if i is a 
#final triplet value, ie all 3 values in triplet exist, increase the
#counter by the number saved in r2. 

def countTriplets(arr, ratio):
    r2 = Counter() #Keep count of potential 2nd and 3rd triplet values
    r3 = Counter()

    triplets = 0
    
    for i in arr:
        if i in r3:
            triplets += r3[i]
        
        if i in r2:
            r3[i*ratio] += r2[i]
        
        r2[i*ratio] += 1

    return triplets


class Test(unittest.TestCase):
    def test_no_repeats(self):
        arr = [1, 2, 4]
        self.assertEqual(countTriplets(arr, 2), 1)

    def test_repeat_first_value(self):
        arr = [1, 1, 3, 9]
        self.assertEqual(countTriplets(arr, 3), 2)

    def test_repeat_second_value(self):
        arr = [10, 20, 20, 40]
        self.assertEqual(countTriplets(arr, 2), 2)

    def test_repeat_third_value(self):
        arr = [10, 30, 90, 90]
        self.assertEqual(countTriplets(arr, 3), 2)

    def test_repeat_multiple_values(self):
        arr = [10, 10, 10, 40, 40, 160]
        self.assertEqual(countTriplets(arr, 4), 6)

    def test_ratio_1(self):
        arr = [1, 1, 1]
        self.assertEqual(countTriplets(arr, 1), 1)

    def test_ratio_1_many(self):
        arr = [1, 1, 1, 1, 1]
        self.assertEqual(countTriplets(arr, 1), 10)
if __name__ == "__main__":
    unittest.main()