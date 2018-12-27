
# Complete the rotLeft function below.
def rotLeft(a, d):
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

input = [1, 2, 3, 4, 5]
print(rotLeft(input, 4))
