#Chapter 4: Trees and Graphs
#4.1 Route Between Nodes, page 109
#Given a directed graph, finds the shortest path between two given nodes.
#Does this by using BFS to search the graph. Starts at node1 and during 
#traversal, checks if node2 is found. Keeps track of nodes that have already
#been visited to avoid cycles and repetition. 

import unittest
from Node import Node

def findPath(node1, node2):
	path = None
	queue = Queue()
	current = node1

	current.shortestPath = [current]
	visited = [current]

	while current:
		for adjacent in current.adjList:
			if not adjacent.shortestPath:
				adjacent.shortestPath = current.shortestPath + [adjacent]
				if adjacent == node2:
					path = current.shortestPath + [adjacent]
					break
				queue.add(adjacent)
				visited.append(adjacent)
		current = queue.remove()
	for v in visited:
	 	v.shortestPath = None
	return path

class Queue():
	def __init__(self):
		self.items = []
	
	def add(self, item):
		self.items.append(item)

	def remove(self):
		if not len(self.items):
			return None
		item = self.items[0]
		del self.items[0]
		return item

def str_for(path):
	if not path: return str(path)
	return ''.join([str(n.value) for n in path])
	
class Test(unittest.TestCase):
	def test_find_path(self):
		f = Node('F')
		e = Node('E')
		d = Node('D', [e])
		c = Node('C', [e])
		b = Node('B', [d, c])
		a = Node('A', [b, c])
		self.assertEqual(str_for(findPath(a, f)), 'None')
		self.assertEqual(str_for(findPath(a, c)), 'AC')
		self.assertEqual(str_for(findPath(a, d)), 'ABD')
		a.add_edge(e)
		self.assertEqual(str_for(findPath(a, e)), 'AE')

if __name__ == "__main__":
	unittest.main()