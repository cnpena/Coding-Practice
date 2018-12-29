#Given an array of integers and a number, d, performs
#d left rotations on the array. Returns the new array

#Works by performing a single rotation at a time, 
#copies the old array in the same order and appends
#the first element of the old array to the end of the
#new array.
#This method is not ideal for larger sets with many rotations

def rotateLeft(a, d):
    current = a
    for i in range(d):
        current = rotateOnce(current)
    return current
    
def rotateOnce(a):
    new = []
    for i in range(1, len(a)):
        new.append(a[i])
    new.append(a[0])
    return new

#Much simpler and efficient way to perform rotation.
#Works by appending a[d] through a[len(a)] to a[0] through a[d]
def rotateLeft2(a, d):
	return a[d:] + a[:d]

input = [1, 2, 3, 4, 5]
print(rotateLeft(input, 4))
print(rotateLeft2(input, 4))
