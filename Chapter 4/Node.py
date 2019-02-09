class Node:
	def __init__(self, value, adjList):
		self.value = value
		self.adjList = adjList

	def add_edge(self, node):
    	self.adjList += [node]
		