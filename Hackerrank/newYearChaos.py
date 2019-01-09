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

def minimumBribes(q):
    bribes = 0
    for index, value in enumerate(q):
        if (value - 1) - index > 2:
            print('Too chaotic')
            return

        for j in range(max(0, q[index] - 2), index):
            if q[j] > q[index]:
                bribes+=1
    print(bribes)
