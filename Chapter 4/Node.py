class Node:
	def __init__(self, value, adjList=None):
		self.value = value
		self.adjList = adjList or []
		self.shortestPath = None
		
	def add_edge(self, node):
		self.adjList += [node]
		