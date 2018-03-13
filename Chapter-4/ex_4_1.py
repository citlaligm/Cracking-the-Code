from Graph import Graph, Node


def Route_nodes(graph):
    if len(graph.nodes) == 0:
        return False
    
    #Implement DFS recursively
    while len(graph.nodes) > 0:
        
    
    
    
    
    
def test_empty():
    #graph = Graph([node(6,'6'), node(5,'5'), node(4,'4')])
    graph = Graph([])

    assert Route_nodes(graph) == False
    
def test_thereis_a_route():
    node6 = Node(6, '6')
    node5 = Node(5, '5')
    node4 = Node(4, '4')

    graph = Graph([node6, node5, node4])
    

    assert Route_nodes(graph) == True