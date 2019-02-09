#Chapter 4: Trees and Graphs
#4.1 Route Between Nodes, page 109
#Given a directed graph, determines whether there is a route between them.
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
	return ''.join([str(n) for n in path])
	
class Test(unittest.TestCase):
	def test_find_route(self):
		node_j = Node('J')
		node_i = Node('I')
		node_h = Node('H')
		node_d = Node('D')
		node_f = Node('F', [node_i])
		node_b = Node('B', [node_j])
		node_g = Node('G', [node_d, node_h])
		node_c = Node('C', [node_g])
		node_a = Node('A', [node_b, node_c, node_d])
		node_e = Node('E', [node_f, node_a])
		node_d.add_edge(node_a)
		self.assertEqual(str_for(findPath(node_a, node_i)), 'None')
		self.assertEqual(str_for(findPath(node_a, node_j)), 'ABJ')
		node_h.add_edge(node_i)
		self.assertEqual(str_for(findPath(node_a, node_i)), 'ACGHI')

if __name__ == "__main__":
	unittest.main()