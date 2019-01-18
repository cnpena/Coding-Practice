#Array Manipulation
#Starting with a 1-indexed array of zeros and a list of operations, 
#for each operation adds a value to each of the array elements between
#two given indices. Once all operations have been performed, returns
#the maximum value in the array.

#To avoid updating every indice and reduce runtime, this solution uses a
#difference array. For each update, only the left and right index are updated.
#The left index is incremented by the proper value and the right index is
#decremented by this value. Then, we are able to use these edges to infer the
#values between them to find each value in the array and ultimately the maximum.

import unittest

def arrayManipulation(n, queries):
    a = [0] * (n+1)

    for i in range(len(queries)):
        l = queries[i][0]
        r = queries[i][1]
        value = queries[i][2]

        a[l-1] += value
        a[r] -= value
  
    return findMax(a)

#Iterates through the array, using the previous value to calculate the value at every 
#index. 
def findMax(arr):
    maxValue = x = 0
    for i in arr:
        x = x + i
        if x > maxValue:
            maxValue = x
    return maxValue

#Tests from Hackerrank
class Test(unittest.TestCase):
    def test1(self):
        arr = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
        self.assertEqual(arrayManipulation(5, arr), 200)

    def test2(self):
        arr = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
        self.assertEqual(arrayManipulation(10, arr), 10)

    def test3(self):
        arr = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]
        self.assertEqual(arrayManipulation(10, arr), 31)
if __name__ == "__main__":
    unittest.main()