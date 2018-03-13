class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        
        
class Node:
    def __init__(self, value, name):
        self.value = value
        self.name = name
        self.adjacents = []        
        self.visited = False
        
        