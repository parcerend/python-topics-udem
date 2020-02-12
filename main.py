from tree import Tree
from graph import Graph, Node, Arc

node_1 = Node('1')
node_2 = Node('2')
node_3 = Node('3')
node_4 = Node('4')
node_5 = Node('5')
node_6 = Node('6')
node_7 = Node('7')
node_8 = Node('8')
node_9 = Node('9')

g1 = Graph(
    [node_1, node_2, node_3, node_4, node_5, node_6, node_7, node_8, node_9],
    [
        Arc(1, node_1, node_2),
        Arc(1, node_1, node_3),
        Arc(1, node_1, node_4),
        Arc(1, node_3, node_5),
        Arc(1, node_3, node_6),
        Arc(1, node_4, node_7),
        Arc(1, node_4, node_8),
        Arc(1, node_8, node_9)
    ]
)

path = g1.find_path(node_1, node_7)
for node in path.get('path'):
    print(node[0].value, node[1])
print(f"Final distance {path.get('distance')}")
