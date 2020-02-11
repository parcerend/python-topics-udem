from tree import Tree
from graph import Graph, Node, Arc

node_a = Node('a')
node_b = Node('b')
node_c = Node('c')
node_d = Node('d')
node_e = Node('e')

g1 = Graph(
    [node_a, node_b, node_c, node_d, node_e],
    [
        Arc(5, node_a, node_d),
        Arc(1, node_d, node_b),
        Arc(4, node_b, node_a),
        Arc(2, node_a, node_c),
        Arc(3, node_d, node_c),
        Arc(6, node_c, node_b),
        Arc(5, node_b, node_e),
        Arc(4, node_d, node_e)
    ]
)

# g1.deep_first_search(node_c, print)
# g1.deep_first_search(node_c, lambda value: print(value ))
# print(g1.neighboors(node_a))
print(g1.dijkstra(node_a, node_e))
print(list(map(lambda node: node.value, g1.breadth_first_search(node_a, node_b))))
