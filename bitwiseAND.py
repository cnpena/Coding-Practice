#Given set S = {1, 2, 3, ..., N}, finds two integers A and B from
#S such that the value of bitwise A&B is the max possible while
#less than given integer K. 
#First line contains integer T, the number of test cases
#Each line following defines a test case as 2 space-separated integers
#N and K.

#Simple solution that works because 
#when k is odd, k-1 is even and can always be reached by (k-1)&k
#when k is even, k-1 is odd and can only be reached if (k-1)or k is <= n

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        
        print(k-1 if ((k-1) | k) <= n else k-2)
