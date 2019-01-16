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

def activityNotifications(expenditure, k):
    count = 0
    KDaysSorted = sorted(expenditure[0:k])

    for i in range(k, len(expenditure)):
        m = median(KDaysSorted)
        KDaysSorted = remove_insert(KDaysSorted, expenditure[i-k], expenditure[i])
        if expenditure[i] >= (2*m):
            count +=1
    return count

def remove_insert(arr, a, b):
    index = bisect.bisect_left(arr, a)
    arr.pop(index)
    bisect.insort_right(arr, b)
    return arr

def median(arr):
    n = len(arr)
    if n % 2 == 1:
        return arr[n//2]
    else:
        return sum(arr[n//2-1:n//2+1])/2.0