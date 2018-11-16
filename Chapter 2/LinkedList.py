class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, data):
		node = Node(data)
		node.next = self.head
		self.head = node

	def printl(self):
		current  = self.head
		while current:
			print(current.data)
			current = current.next

	#For testing purposes
	def asList(self):
		current = self.head
		list = []
		while current:
			list.append(current.data)
			current = current.next
		return list

	def findNode(self,value):
		current = self.head
		while current:
			if current.data == value:
				return current
			current = current.next
		return None

	def length(self):
		current = self.head
		length = 0
		while current:
			length +=1
			current = current.next
		return length