from Graph import Graph, Node
from collections import deque

def Route_nodes(graph, init_node=None, end_node=None):
    if len(graph.nodes) == 0:
        return False
    
    if (init_node.name == end_node.name):
        return True
    
    #Implement DFS recursively
    for node in init_node.adjacents:       
        if not node.visited:  
            node.visited = True  
            return Route_nodes(graph, node, end_node)
   
    return False
    
    
def Route_bfs_deque(graph, init_node=None, end_node=None, queue=deque()):
    
    init_node.visited = True
    queue.append(init_node)
    
    while queue:
        node = queue.pop()
        if (node.name == end_node.name):
            return True
        for node in node.adjacents:
            if node.visited == False:
                queue.append(node)
                node.visited = True
        
    
    return False
    
    
def test_empty():
    #graph = Graph([node(6,'6'), node(5,'5'), node(4,'4')])
    graph = Graph([])

    assert Route_nodes(graph) == False
    
def test_base_case():
    node6 = Node(6, '6')
    node5 = Node(5, '5')
    node4 = Node(4, '4')

    node6.adjacents = [node5]
    node5.adjacents = [node4]
    node4.adjacents = [node6]
    
    graph = Graph([node6, node5, node4])
    

    assert Route_nodes(graph, node6, node6) == True

def test_thereis_a_path():
    node6 = Node(6, '6')
    node5 = Node(5, '5')
    node4 = Node(4, '4')

    node6.adjacents = [node5]
    node5.adjacents = [node4]
    node4.adjacents = [node6]
    
    graph = Graph([node6, node5, node4])
    

    assert Route_nodes(graph, node6, node4) == True

def test_thereis_nota_path_dfs():
    node6 = Node(6, '6')
    node5 = Node(5, '5')
    node4 = Node(4, '4')
    node3 = Node(3, '3')
    node2 = Node(2, '2')

    node6.adjacents = [node5]
    node5.adjacents = [node3]
    node4.adjacents = [node2]
    
    graph = Graph([node6, node5, node4, node3])
    

    assert Route_nodes(graph, node6, node4) == False
    #assert Route_bfs_deque(graph, node6, node4) == False
    
    
def test_thereis_nota_path_bfs():
    node6 = Node(6, '6')
    node5 = Node(5, '5')
    node4 = Node(4, '4')
    node3 = Node(3, '3')
    node2 = Node(2, '2')

    node6.adjacents = [node5]
    node5.adjacents = [node3]
    node4.adjacents = [node2]
    
    graph = Graph([node6, node5, node4, node3])
    

    assert Route_bfs_deque(graph, node6, node4) == False
    
    


