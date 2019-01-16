#Fraudulent Activity Notifications

#Given k number of trailing days and a client's total daily expenditures for a period of days,
#prints the number of times the client will receive a notification over all days.
#Notifications are sent as follows: If the amount spent by a client on a particular day is greater
#than or equal to two times the client's median spending for k trailing days, a notification is sent.
#Note that notifications are not sent until they have at least k trailing number of prior days' data.

#The easiest way to do this is trivial. Return the median for the past k days and compare to day i.
#This program, however, optimizes this method since it requires the list to be sorted each time the 
#median is calculated.

#To avoid sorting each time the median is calculated, the list is sorted once at the beginning.
#Then, notice that each time the median is calculated, only two values change, the current value
#is added to the kDays array and the value k days before is removed from the kDays array. Therefore, 
#we make use of Python bisect which allows us to remove and insert the values without having to sort. 

import bisect
import unittest

def activityNotifications(expenditure, k):
    count = 0
    KDaysSorted = sorted(expenditure[0:k])

    for i in range(k, len(expenditure)):
        m = median(KDaysSorted)
        KDaysSorted = remove_insert(KDaysSorted, expenditure[i-k], expenditure[i])
        if expenditure[i] >= (2*m):
            count +=1
    return count

#Given a sorted array, removes a from the array and inserts b in its proper position. Returns a sorted array.
def remove_insert(arr, a, b):
    index = bisect.bisect_left(arr, a)
    arr.pop(index)
    bisect.insort_right(arr, b)
    return arr

#Given a sorted array, returns the median value. If odd length, the exact middle value. If even length, 
#returns the average of the two middle values.
def median(arr):
    n = len(arr)
    if n % 2 == 1:
        return arr[n//2]
    else:
        return sum(arr[n//2-1:n//2+1])/2.0

class Test(unittest.TestCase):
    def test_1(self):
        arr = [2, 3, 4, 2, 3, 6, 8, 4, 5]
        self.assertEqual(activityNotifications(arr, 5), 2)

    def test_2(self):
        arr = [1, 2, 3, 4, 4]
        self.assertEqual(activityNotifications(arr, 4), 0)

    def test_3(self):
        arr = [10, 20, 30, 40, 50]
        self.assertEqual(activityNotifications(arr, 4), 1)

if __name__ == "__main__":
    unittest.main()