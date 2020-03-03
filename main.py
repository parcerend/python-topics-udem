from tree import Tree
from graph import Graph, Node, Arc

node_mail = Node('Mail', 0)
node_ts = Node('ts', 4)
node_103 = Node('103', 3)
node_b3 = Node('b3', 3)
node_b1 = Node('b1', 2)
node_c2 = Node('c2', 3)
node_c1 = Node('c1', 7)
node_c3 = Node('c3', 0)
node_b2 = Node('b2', 2)
node_b4 = Node('b4', 6)
node_109 = Node('109', 3)
node_111 = Node('111', 0)
node_119 = Node('119', 6)
node_storage = Node('storage', 0)
node_123 = Node('123', 3)
node_123r = Node('123r', 0)
node_125 = Node('125', 0)

g1 = Graph(
    [node_mail, node_ts, node_103, node_b3, node_b1, node_c2, node_c1, node_c3, node_b2, node_b4, node_109, node_111, node_119, node_storage, node_123, node_123r, node_125],
    [
        Arc(8, node_103, node_ts),
        Arc(12, node_103, node_109),
        Arc(4, node_103, node_b3),
        Arc(6, node_ts, node_mail),
        Arc(4, node_b3, node_b1),
        Arc(7, node_b3, node_b4),
        Arc(3, node_b1, node_c2),
        Arc(6, node_b1, node_b2),
        Arc(6, node_c2, node_c3),
        Arc(4, node_c2, node_c1),
        Arc(8, node_c1, node_c3),
        Arc(3, node_b2, node_b4),
        Arc(7, node_b4, node_109),
        Arc(4, node_109, node_111),
        Arc(16, node_109, node_119),
        Arc(7, node_119, node_storage),
        Arc(9, node_119, node_123),
        Arc(4, node_123, node_123r),
        Arc(4, node_123, node_125),
        Arc(2, node_b3, node_b2)
    ]
)

path = g1.find_path(node_103, node_123r)
print(path.get('distance'))
print(g1.iterative_search(node_103, node_123r, 5))
for node in path.get('path'):
    print(node[0].value)

