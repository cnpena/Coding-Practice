#Chapter 2: Linked Lists
#2.5 Sum Lists, page 95
#Adds two numbers, represented by linked list where each node 
#contains a single digit. Returns the sum as a linked list
#Example:
#	Input: (7 -> 1 -> 6) + (5 -> 9 -> 2) 617+295
#	Output: (2 -> 1 -> 9) 912
from LinkedList import LinkedList
from LinkedList import Node
import unittest

#Simple add function, works by iterating through the two linked lists,
#appending each data value to a string. At the end, each string is 
#converted to an int representing the whole linked list.
#Then, we can simply add them using the + operator.
def simpleAdd(one, two):
	num1 = getNumberAsInt(one)
	num2 = getNumberAsInt(two)
	sum = num1+num2

	list = LinkedList()
	for digit in str(sum):
		list.insert(int(digit))
	return list

def getNumberAsInt(list):
	current = list.head
	num = ''
	while(current):
		num = str(current.data) + num
		current = current.next
	return int(num)

#Non-recursive add function. Starts at the head of each list and adds until
#there are no more digits to add. Stores each digit of the solution as a node
#in the 'sum' linked list.
def add(num1, num2):
	sum = LinkedList()
	current1 = num1.head
	current2 = num2.head
	carry = 0
	result = 0

	while(current1 or current2 or carry):
		result = carry
		if(current1):
			result += current1.data
			current1 = current1.next
		if(current2):
			result += current2.data
			current2 = current2.next
		result, carry = returnCarry(result)
		sum.insertTail(result)

	return sum.asList()

def returnCarry(result):
	carry = 0
	if(result >= 10):
		result = result - 10
		carry = 1
	return result, carry

#Recursive add function: Adds node by node, carrying over any excess data to the next node
def addRec(num1, num2, carry):
	if(not num1 and not num2 and carry == 0):
		return None

	result = Node(0)
	value = carry
	if(num1):
		value += num1.data
	if(num2):
		value += num2.data

	result.data = value % 10

	if(num1 or num2):
		result.next = addRec(num1.next if num1 else None, num2.next if num2 else None, 1 if value >= 10 else 0)
	print(result.data)

class Test(unittest.TestCase):
    num1 = LinkedList()
    num2 = LinkedList()
    num3 = LinkedList()

    num1.insert(6)
    num1.insert(1)
    num1.insert(7)

    num2.insert(2)
    num2.insert(3)

    sol1 = [4, 3, 2, 1]
    sol2 = [0, 4, 6]

    testCases = [(num1, num1, sol1),
    			(num1, num2, sol2),
    			(num2, num1, sol2)]

    def testSum(self):
        for [num1, num2, expected] in self.testCases:
            self.assertEqual(simpleAdd(num1, num2).asList(), expected)
            self.assertEqual(add(num1, num2), expected)

if __name__ == "__main__":
    unittest.main()
