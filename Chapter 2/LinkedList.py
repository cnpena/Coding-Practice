class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def __len__(self):
		length = 0
		current = self.head
		while current:
			length += 1
			current = current.next
		return length

	def insert(self, data):
		if self.head is None:
			self.tail = self.head = Node(data)
		else:
			node = Node(data)
			node.next = self.head
			self.head = node

	def insertTail(self, data):
		if self.head is None:
			self.tail = self.head = Node(data)
		else:
			node = Node(data)
			self.tail.next = node
			self.tail = node

	def printl(self):
		current = self.head
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

	def findNode(self, value):
		current = self.head
		while current:
			if current.data == value:
				return current
			current = current.next
		return None