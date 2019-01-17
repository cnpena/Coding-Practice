#Array Manipulation
#Starting with a 1-indexed array of zeros and a list of operations, 
#for each operation adds a value to each of the array elements between
#two given indices. Once all operations have been performed, returns
#the maximum value in the array.

import unittest

def arrayManipulation(n, queries):
    a = [0] * (n+1)
    print(a)

    for i in range(len(queries)):
        l = queries[i][0]
        r = queries[i][1]
        value = queries[i][2]

        a[l-1] += value
        if r <= len(a):
            a[r] -= value
        print(a)
    return findMax(a)

def findMax(arr):
    maxValue = x = 0
    for i in arr:
        x = x + i
        if x > maxValue:
            maxValue = x
    return maxValue
